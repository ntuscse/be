from fastapi import FastAPI
from mangum import Mangum
import os

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


handler = Mangum(app)
