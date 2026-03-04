from fastapi import FastAPI
from app.api.webhook import router

app=FastAPI(title="kritrim", version="0.1.0")

app.include_router(router)

@app.get("/")
def first():
    return {"message":"Kritrim is alive"}
