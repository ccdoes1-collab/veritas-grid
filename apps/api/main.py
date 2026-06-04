# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/identity")
def get_identity():
    return {"message": "Identity service placeholder"}