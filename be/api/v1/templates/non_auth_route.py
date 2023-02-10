import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

stage = os.environ.get('SERVERLESS_STAGE')
is_dev = stage == "dev"
prod = stage == "prod"

origins= []
if stage == "prod":
    origins = [
        "https://merch.ntuscse.com",
        "https://ntuscse.com",
        "https://api.docs.ntuscse.com"
    ]
else:
    origins = ["*"]

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
