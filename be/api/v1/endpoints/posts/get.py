from fastapi import APIRouter, HTTPException

from be.api.v1.templates.nonAuthRoute import createNonAuthRouter
from be.api.v1.fixtures.post_data import dummy_posts

router = APIRouter(prefix="/posts")


@router.get("")
def get_posts():
    return dummy_posts


@router.get("/{post_id}")
def get_post(post_id: str):
    for post in dummy_posts:
        if post['id'] == post_id:
            return post

    # no matching post found
    raise HTTPException(status_code=404, detail="Post not found")


handler = createNonAuthRouter(router)
