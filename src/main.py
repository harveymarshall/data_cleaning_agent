from fastapi import FastAPI

app = FastAPI()

from .routes.invoke import invoke

@app.get("/")
async def root():
    return {"message": "Welcome to the data cleaning agent"}

app.post("/invoke")(invoke)
