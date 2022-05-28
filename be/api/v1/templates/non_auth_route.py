from fastapi import FastAPI
from mangum import Mangum


def create_non_auth_router(router):
    app = FastAPI()
    app.include_router(router)

    mangum_instance = Mangum(app)

    return mangum_instance
