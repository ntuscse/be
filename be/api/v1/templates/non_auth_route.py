import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

is_dev = os.environ.get('SERVERLESS_STAGE')

origins = [
    "http://localhost:3000",
    "https://dev.ntuscse.com",
] if is_dev else [
    "https://ntuscse.com",
]


def create_non_auth_router(router):
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)

    mangum_instance = Mangum(app)

    return mangum_instance
