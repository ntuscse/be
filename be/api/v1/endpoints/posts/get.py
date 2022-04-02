from fastapi import APIRouter, HTTPException

from be.api.v1.templates.nonAuthRoute import createNonAuthRouter


router = APIRouter(prefix="/posts")

dummy_posts = [
    {"id": "1", "title": "post title1", "content": "this is some post content1"},
    {"id": "2", "title": "post title2", "content": "this is some post content2"},
    {"id": "3", "title": "post title3", "content": "this is some post content3"},
    {"id": "4", "title": "post title4", "content": "this is some post content4"},
    {"id": "5", "title": "post title5", "content": "this is some post content5"},
]


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
