from io import BytesIO, StringIO
import pandas as pd
from fastapi import UploadFile

async def load_uploaded_file(file: UploadFile) -> pd.DataFrame:
    """
    Load an uploaded file into a pandas DataFrame.

    Args:
        file: The uploaded file object.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    contents = await file.read()
    if file.filename.endswith('.csv'):
        return pd.read_csv(StringIO(contents.decode('utf-8')))
    elif file.filename.endswith(('.xlsx', '.xls')):
        return pd.read_excel(BytesIO(contents))
    elif file.filename.endswith('.json'):
        return pd.read_json(StringIO(contents.decode('utf-8')))
    elif file.filename.endswith('.parquet'):
        return pd.read_parquet(BytesIO(contents))
    else:
        raise ValueError("Unsupported file format. Please upload a CSV, Excel, JSON, or Parquet file.")
