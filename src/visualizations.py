import plotly.express as px

def generate_chart(df, parsed):
    """
    Generates a Plotly chart based on parsed query info.

    Args:
        df (pd.DataFrame): DataFrame containing data to visualize.
        parsed (dict): Parsed query dict with keys:
            - 'visualization' (str): 'bar', 'histogram', 'line', 'none'
            - 'column' (str): column to visualize
            - 'operation' (str): 'count', 'mean', etc.

    Returns:
        plotly.graph_objs._figure.Figure or None: Plotly figure or None if no chart.
    """
    viz = parsed.get('visualization', 'none')
    col = parsed.get('column')
    op = parsed.get('operation')

    if viz == 'none' or col is None:
        return None

    has_count = 'count' in df.columns

    if viz == 'bar':
        if has_count:
            fig = px.bar(df, x=col, y='count', title=f"Bar chart of count by {col}")
            fig.update_layout(xaxis_title=col, yaxis_title="Count")
        else:
            fig = px.bar(df, x=col, y=col, title=f"Bar chart of {col}")
            fig.update_layout(xaxis_title=col, yaxis_title=col)
        return fig

    elif viz == 'histogram':
        fig = px.histogram(df, x=col, title=f"Histogram of {col}")
        fig.update_layout(xaxis_title=col, yaxis_title="Frequency")
        return fig

    elif viz == 'line':
        if has_count:
            fig = px.line(df, x=col, y='count', title=f"Line chart of count by {col}")
            fig.update_layout(xaxis_title=col, yaxis_title="Count")
            return fig
        else:
            # For raw numeric data, plot column over index
            if col in df.columns and df[col].dtype.kind in 'biufc':  # numeric types
                fig = px.line(df, y=col, title=f"Line chart of {col}")
                fig.update_layout(xaxis_title="Index", yaxis_title=col)
                return fig
            return None

    else:
        return None
