from fastapi import APIRouter, HTTPException
from be.api.v1.models.posts import Post
from be.api.v1.templates.nonAuthRoute import createNonAuthRouter
from be.api.v1.fixtures.post_data import dummy_posts

router = APIRouter(prefix="/posts")


@router.get("",
            response_model=list[Post],
            summary="Get posts",
            description="Gets a list of posts from the db",
            tags={"posts"}
            )
def get_posts(
):
    return dummy_posts


@router.get("/{post_id}",
            response_model=Post,
            summary="Get a post",
            description="Gets a single posts from the db, specified by post_id",
            tags={"posts"}
            )
def get_post(post_id: str):
    for post in dummy_posts:
        if post['id'] == post_id:
            return post

    # no matching post found
    raise HTTPException(status_code=404, detail="Post not found")


handler = createNonAuthRouter(router)
