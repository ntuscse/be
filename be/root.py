from fastapi import FastAPI
from be.api.v1.endpoints.posts import get as posts_get, post as posts_post, patch as posts_patch, delete as posts_delete


# this file is for documentation & local development use

app = FastAPI()

app.include_router(posts_get.router)
app.include_router(posts_post.router)
app.include_router(posts_patch.router)
app.include_router(posts_delete.router)
