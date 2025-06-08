import pytest
from src.excel_parser import load_excel

def test_load_excel():
    df, dtypes, error = load_excel("tests/sample_data/sample1.xlsx")
    assert df is not None
    assert len(df.columns) > 0
    assert error is None
    assert all('_' in c or c.isalnum() for c in df.columns)  # Check normalization

def test_invalid_file():
    df, dtypes, error = load_excel("tests/sample_data/invalid.txt")
    assert df is None
    assert error is not None