import pandas as pd

class ExcelParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.dataframe = None

    def load_excel(self):
        """Load Excel file into a pandas DataFrame."""
        try:
            self.dataframe = pd.read_excel(self.file_path)
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
        """Filter data where column_name equals value."""
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


# Example usage
if __name__ == "__main__":
    parser = ExcelParser("sample_data.xlsx")
    parser.load_excel()
    print("Columns:", parser.get_columns())
    data = parser.get_data()
    if data is not None:
        print(data.head())

    filtered = parser.filter_data("Category", "Electronics")
    if filtered is not None:
        print(filtered)
