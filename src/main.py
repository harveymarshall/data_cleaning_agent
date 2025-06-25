from fastapi import FastAPI

app = FastAPI()

from .routes.invoke import invoke
from .routes.health_check import health_check

@app.get("/")
async def root():
    return {"message": "Welcome to the data cleaning agent"}

app.post("/invoke")(invoke)
app.get("/health")(health_check)
