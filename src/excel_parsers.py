import pandas as pd

class ExcelParser:
    def __init__(self, file_path, sheet_name=None):
        """
        Initialize ExcelParser with file path and optional sheet name.

        Args:
            file_path (str): Path to the Excel file.
            sheet_name (str, optional): Sheet name or index to load. Defaults to None (first sheet).
        """
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.dataframe = None

    def load_excel(self):
        """Load Excel file into a pandas DataFrame."""
        try:
            self.dataframe = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
            print(f"Excel file '{self.file_path}' loaded successfully.")
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        except Exception as e:
            print(f"An error occurred while loading Excel file: {e}")

    def get_columns(self):
        """Return list of columns in the Excel sheet."""
        if self.dataframe is not None:
            return self.dataframe.columns.tolist()
        else:
            print("Dataframe is empty. Load the Excel file first.")
            return []

    def get_data(self):
        """Return the whole data as a DataFrame."""
        if self.dataframe is not None:
            return self.dataframe
        else:
            print("Dataframe is empty. Load the Excel file first.")
            return None

    def filter_data(self, column_name, value):
        """
        Filter data where column_name equals value.

        Args:
            column_name (str): Column to filter on.
            value: Value to filter by.

        Returns:
            pd.DataFrame or None: Filtered DataFrame or None if error.
        """
        if self.dataframe is not None:
            if column_name in self.dataframe.columns:
                filtered_df = self.dataframe[self.dataframe[column_name] == value]
                return filtered_df
            else:
                print(f"Column '{column_name}' does not exist in the data.")
                return None
        else:
            print("Dataframe is empty. Load the Excel file first.")
            return None


def load_excel_file(file):
    """
    Load an Excel file into a DataFrame and return its data types.

    Args:
        file (str): Path to the Excel file.

    Returns:
        tuple: (DataFrame or None, dict of column data types or None, error message or None)
    """
    try:
        df = pd.read_excel(file)
        dtypes = {col: str(dtype) for col, dtype in df.dtypes.items()}
        return df, dtypes, None
    except Exception as e:
        return None, None, str(e)


# Example usage
if __name__ == "__main__":
    parser = ExcelParser("sample_data.xlsx")
    parser.load_excel()
    
    cols = parser.get_columns()
    print("Columns:", cols)
    
    data = parser.get_data()
    if data is not None:
        print(data.head())

    filtered = parser.filter_data("Category", "Electronics")
    if filtered is not None:
        print("Filtered Data:")
        print(filtered)

    # Using standalone function
    df, dtypes, err = load_excel_file("sample_data.xlsx")
    if err:
        print(f"Error loading Excel file: {err}")
    else:
        print("Standalone function loaded columns:", df.columns.tolist())
        print("Data types:", dtypes)
