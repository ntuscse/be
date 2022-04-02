
from typing import Optional

from fastapi import APIRouter, File, Form, UploadFile


router = APIRouter(prefix="/posts")


@router.patch("/{post_id}")
async def patch_post(
    post_id: str,
    title: Optional[str] = Form(None),
    body: Optional[str] = Form(None),
    author: Optional[str] = Form(None),  # todo: should we get this from auth?
    categories: Optional[str] = Form(None),
    images: Optional[list[UploadFile]] = File(None)
):
    # todo: upload image blobs to s3

    # todo: lookup post by post_id

    # update post with form data

    return {
        "status": "Post created successfully",
        "update": {
            title, body, author, categories, images
        },
        "updatedPost": {
            "id": post_id,
            "title": title,
            "body": body,
            "author": author,
            "categories": categories,
        }
    }
