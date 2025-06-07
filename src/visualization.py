import plotly.express as px

def generate_chart(df, parsed):
    """
    Generates a Plotly chart based on parsed query info.
    """
    viz = parsed.get('visualization', 'none')
    col = parsed.get('column')
    op = parsed.get('operation')

    if viz == 'none' or col is None:
        return None

    # For count/group_by data, df should have col and 'count' columns
    if viz == 'bar':
        if 'count' in df.columns:
            fig = px.bar(df, x=col, y='count', title=f"Bar chart of count by {col}")
        else:
            fig = px.bar(df, x=col, y=col, title=f"Bar chart of {col}")
        fig.update_layout(xaxis_title=col, yaxis_title="Count")
        return fig

    elif viz == 'histogram':
        fig = px.histogram(df, x=col, title=f"Histogram of {col}")
        fig.update_layout(xaxis_title=col, yaxis_title="Frequency")
        return fig

    elif viz == 'line':
        if 'count' in df.columns:
            fig = px.line(df, x=col, y='count', title=f"Line chart of count by {col}")
            fig.update_layout(xaxis_title=col, yaxis_title="Count")
            return fig
        else:
            return None

    else:
        return None
