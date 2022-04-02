from fastapi import FastAPI
from mangum import Mangum


def createAuthRouter(router):
    # todo: add jwt auth middleware
    app = FastAPI()
    app.include_router(router)

    mangumInstance = Mangum(app)

    return mangumInstance
