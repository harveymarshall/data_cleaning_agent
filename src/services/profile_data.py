import pandas as pd
from fastapi import UploadFile
from ..services.load_data import load_uploaded_file

async def profile_data(file: UploadFile, max_cols=100):
    """_summary_

    Args:
        df (pd.DataFrame): DataFrame of the loaded dataset to summarize.
        max_cols (int, optional): Number of columns to load from df to return in the summary DataFrame. Defaults to 100.

    Returns:
        pd.DataFrame: Returned is a DataFrame with the summary values from the profiling action either 100 cols if no max_cols values passed.
    """
    df = await load_uploaded_file(file)
    summary = df.describe(include='all').transpose()
    summary['missing_values'] = df.isnull().sum()
    return {"Summary": summary.head(max_cols).to_string()}
