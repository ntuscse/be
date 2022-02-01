from fastapi import FastAPI
from mangum import Mangum
import os


def createNonAuthRouter(router):
    stage = os.environ.get('STAGE', 'dev')  # ???

    app = FastAPI()
    app.include_router(router)

    mangumInstance = Mangum(app)

    return mangumInstance
