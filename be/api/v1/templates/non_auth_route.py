from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import os

is_offline = os.environ.get('IS_OFFLINE')

origins = [
    "http://localhost:4000",
] if is_offline else [
    "https://api.ntuscse.com",
    "https://api.dev.ntuscse.com",
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
