from fastapi import FastAPI
from mangum import Mangum
from be.api.v1.endpoints.posts import get as posts_get, post as posts_post, patch as posts_patch


app = FastAPI()

# this file is for local development and non-serveless use

app.include_router(posts_get.router)
app.include_router(posts_post.router)
app.include_router(posts_patch.router)


# handler = Mangum(app)
