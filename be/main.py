from fastapi import FastAPI
from mangum import Mangum
import os

from be.api.v1.router import router as api_v1_router

stage = os.environ.get('STAGE', 'dev')

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


app.include_router(api_v1_router, prefix="/api/v1")

handler = Mangum(app)
