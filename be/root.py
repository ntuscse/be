from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


handler = Mangum(app)
