from fastapi import FastAPI, Cookie
from typing import Optional
from uuid import uuid4

app = FastAPI()
uuid = uuid4()


@app.get("/api/v1/uuid")
async def root(key: Optional[str] = Cookie(None)):
    print(key)
    return {'uuid_new': uuid}


@app.get("/healthz")
async def health_check():
    return {}