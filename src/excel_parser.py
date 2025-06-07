import pandas as pd

def load_excel(file):
    try:
        df = pd.read_excel(file)
        dtypes = {col: str(dtype) for col, dtype in df.dtypes.items()}
        return df, dtypes, None
    except Exception as e:
        return None, None, str(e)
