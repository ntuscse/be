from fastapi import FastAPI
from mangum import Mangum
from be.api.v1.endpoints.posts import get as posts_get

app = FastAPI()

# this file is for local development and non-serveless use

app.include_router(posts_get.router)


# handler = Mangum(app)
