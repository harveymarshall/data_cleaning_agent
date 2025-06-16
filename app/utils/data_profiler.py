import pandas as pd

def profile_data(df: pd.DataFrame, max_cols=100) -> pd:
    summary = df.describe(include='all').transpose()
    summary['missing_values'] = df.isnull().sum()
    return summary.head(max_cols).to_string()

