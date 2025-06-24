import pandas as pd
from fastapi import UploadFile
from ..main import app
from ..services.invoke_llm import invoke_llm

@app.post("/invoke")
def invoke(file: UploadFile, context: str, role: str):
    return invoke_llm(file, context, role)
