import json
import ollama
from src.visualization import generate_chart
from src.utils import normalize_column_name

def parse_query(query):
    """
    Use Ollama to parse a natural language query into a structured operation.
    Returns: JSON dict with operation, column, filter, visualization.
    """
    prompt = f"""
    Convert the query to a pandas operation. Query: "{query}"
    Return JSON with:
    - operation: 'mean', 'count', 'group_by', or 'none'
    - column: target column name (match fuzzily if needed)
    - filter: condition like 'age < 30' or null
    - visualization: 'bar', 'histogram', 'line', or 'none'
    Example: "What is the average salary?" -> {{"operation": "mean", "column": "salary", "filter": null, "visualization": "none"}}
    """

    try:
        response = ollama.generate(model="mistral", prompt=prompt)
        text = response['response']

        # Extract JSON enclosed in ```json ... ```
        import re
        json_match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            # fallback: extract from first { to last }
            start = text.find('{')
            end = text.rfind('}') + 1
            json_str = text[start:end]

        parsed = json.loads(json_str)
        return parsed
    except Exception as e:
        print(f"Error during query parsing: {e}")
        return {"operation": "none", "column": None, "filter": None, "visualization": "none"}


def process_query(df, parsed):
    """
    Process a query and return result and chart (if any).
    Returns: (result string or DataFrame, Plotly figure or None)
    """
    try:
        # Normalize all df columns once
        normalized_columns = {normalize_column_name(c): c for c in df.columns}
        
        col_key = None
        if parsed.get('column'):
            parsed_col_norm = normalize_column_name(parsed['column'])
            # Find closest matching column key
            for norm_col, orig_col in normalized_columns.items():
                if parsed_col_norm in norm_col:
                    col_key = orig_col
                    break
            if col_key is None:
                return f"Column '{parsed['column']}' not found in data.", None

        op = parsed.get('operation', 'none')
        filter_cond = parsed.get('filter')
        viz = parsed.get('visualization', 'none')

        if op == 'mean':
            result = df[col_key].mean()
            return f"The average {col_key} is {result:.2f}", None

        elif op == 'count':
            if filter_cond:
                try:
                    filtered_df = df.query(filter_cond)
                    count = len(filtered_df)
                    return f"There are {count} matching records", None
                except Exception as e:
                    return f"Invalid filter condition: {filter_cond}", None
            else:
                # Count of unique values
                data = df.groupby(col_key).size().reset_index(name='count')
                chart = generate_chart(data, {'operation': 'count', 'column': col_key, 'visualization': viz})
                return data, chart

        elif op == 'group_by':
            data = df.groupby(col_key).size().reset_index(name='count')
            chart = generate_chart(data, {'operation': 'group_by', 'column': col_key, 'visualization': viz})
            return data, chart

        else:
            return "Query not supported", None

    except Exception as e:
        return f"Error processing query: {str(e)}", None
