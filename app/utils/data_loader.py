import pandas as pd
import io


def load_uploaded_file(file):
    """
    Load an uploaded file into a pandas DataFrame.

    Args:
        file: The uploaded file object.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith(('.xlsx', '.xls')):
        return pd.read_excel(file)
    elif file.name.endswith('.json'):
        return pd.read_json(file)
    elif file.name.endswith('.parquet'):
        return pd.read_parquet(file)
    else:
        raise ValueError("Unsupported file format. Please upload a CSV, Excel, JSON, or Parquet file.")

