import streamlit as st
import pandas as pd
from src.utils import normalize_column_name, suggest_queries
from src.query_processors import process_query, parse_query
from src.visualizations import generate_chart

st.set_page_config(page_title="NeoStats Excel Chatbot", layout="wide")

st.title("NeoStats Excel Insights Chatbot")
st.markdown(
    "Upload an Excel file and ask natural language questions to get instant insights with text, tables, and charts."
)

# Upload & load data
if 'df' not in st.session_state:
    st.session_state.df = None

def handle_upload():
    uploaded_file = st.file_uploader("Upload your Excel file (.xlsx)", type=["xlsx"])
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.success(f"Loaded Excel file with {df.shape[0]} rows and {df.shape[1]} columns.")
            return df
        except Exception as e:
            st.error(f"Error loading Excel file: {e}")
    return None

if st.session_state.df is None:
    df = handle_upload()
    if df is not None:
        st.session_state.df = df
        # Normalize columns internally
        st.session_state.df.columns = [normalize_column_name(col) for col in df.columns]
else:
    df = st.session_state.df
    st.markdown(f"**Current data loaded:** {df.shape[0]} rows, {df.shape[1]} columns")

if df is not None:

    # Preview data
    with st.expander("Preview data"):
        st.dataframe(df.head())

    # Sidebar: Debug toggle + Query suggestions + Clear history
    st.sidebar.header("Options")
    show_debug = st.sidebar.checkbox("Show debug info")
    if st.sidebar.button("Clear Query History"):
        st.session_state.history = []

    st.sidebar.header("Try a suggested query:")
    suggestions = suggest_queries(df)[:5]  # limit suggestions to 5
    for q in suggestions:
        if st.sidebar.button(q):
            st.session_state.query = q

    # Input query box
    query = st.text_input(
        "Ask your question about the data:",
        value=st.session_state.get('query', ''),
        placeholder="E.g., What is the average sales? Show a bar chart of count by region.",
    )
    st.session_state.query = query

    if st.button("Get Insight") and query.strip() != "":
        with st.spinner("Processing your query..."):
            try:
                parsed = parse_query(query)
                if show_debug:
                    st.write(f"Parsed query dict: {parsed}")

                result, chart_fig = process_query(df, parsed)

                # Display text or table result
                if isinstance(result, pd.DataFrame):
                    st.markdown("### Table Result:")
                    st.dataframe(result)
                else:
                    st.markdown(f"### Result: {result}")

                # Display chart or fallback message
                if chart_fig is not None:
                    st.markdown("### Visualization:")
                    st.plotly_chart(chart_fig, use_container_width=True)
                else:
                    st.info("No visualization available for this query.")

                # Save to chat history
                if "history" not in st.session_state:
                    st.session_state.history = []
                st.session_state.history.append((query, str(result)))

            except Exception as e:
                st.error(f"Error processing query: {e}")
                if "history" not in st.session_state:
                    st.session_state.history = []
                st.session_state.history.append((query, f"Error: {e}"))

    # Show chat history limited to last 10
    st.markdown("### Query History")
    if "history" in st.session_state:
        for i, (q, a) in enumerate(st.session_state.history[-10:], 1):
            st.markdown(f"**Q{i}:** {q}")
            st.markdown(f"**A{i}:** {a}")

else:
    st.info("Please upload an Excel file to start asking questions.")

# Footer
st.markdown("---")
st.markdown("© NeoStats | Built with Streamlit")
