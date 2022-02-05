from fastapi import FastAPI
from mangum import Mangum
import os


def createNonAuthRouter(router):
    app = FastAPI()
    app.include_router(router)

    mangumInstance = Mangum(app)

    return mangumInstance
