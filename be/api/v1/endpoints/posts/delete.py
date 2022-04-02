from fastapi import APIRouter, HTTPException

from be.api.v1.fixtures.post_data import dummy_posts


router = APIRouter(prefix="/posts")


@router.delete("/{post_id}")
async def delete_post(post_id: str):

    for post in dummy_posts:
        if post_id == post['id']:
            # todo: remove post from db, remove images from s3
            return {"status": "Post deleted successfully"}

    raise HTTPException(status_code=204, detail="Post not found")
