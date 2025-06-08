import pytest
import pandas as pd
from src.query_processor import process_query

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'salary': [50000, 60000, 75000],
        'department': ['HR', 'IT', 'Sales'],
        'age': [25, 30, 35]
    })

def test_mean_query(sample_df):
    result, chart = process_query(sample_df, "What is the average salary?")
    assert "The average salary is" in result
    assert chart is None

def test_group_by_query(sample_df):
    result, chart = process_query(sample_df, "Show a bar chart of count by department")
    assert "Table:" in result
    assert chart is not None