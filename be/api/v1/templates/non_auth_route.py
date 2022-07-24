from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

origins = [
    "https://api.ntuscse.com",
    "https://api.dev.ntuscse.com",
    "http://localhost",
    "http://localhost:4000",
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
