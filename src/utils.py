def normalize_column_name(col):
    """Normalize column names for internal use."""
    import re
    col = col.lower().replace(' ', '_')
    col = re.sub(r'[^a-z0-9_]', '', col)
    return col

def suggest_queries(df):
    """Generate query suggestions based on DataFrame columns and types."""
    suggestions = []
    for col, dtype in df.dtypes.items():
        if dtype in ['int64', 'float64']:
            suggestions.append(f"What is the average {col}?")
            suggestions.append(f"Show a histogram of {col}")
        elif dtype == 'object':
            suggestions.append(f"Show a bar chart of count by {col}")
        if 'date' in col.lower():
            suggestions.append(f"Show a line chart of count by {col}")
    return suggestions
