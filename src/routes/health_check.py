from ..main import app
from fastapi import status
from pydantic import BaseModel

class HealthCheck(BaseModel):
    status: str = "OK"

@app.get("/health")
def health_check():
    return HealthCheck(status="OK")
