
from re import S
from typing import Optional, Set

from fastapi import APIRouter, File, Form, UploadFile
from pydantic import BaseModel

from be.api.v1.models.posts import PostCategory


router = APIRouter(prefix="/posts")


class UpdatedPost(BaseModel):
    id: str
    title: str
    body: str
    author: str
    category: list[PostCategory]


class Response(BaseModel):
    status: str
    update: Set
    UpdatedPost: UpdatedPost


@router.patch("/{post_id}",
              #   response_model=Response,
              summary="Patch a post",
              description="Updates a single post in the db, specified by post_id",
              tags={"posts"}
              )
async def patch_post(
    post_id: str,
    title: Optional[str] = Form(None),
    body: Optional[str] = Form(None),
    author: Optional[str] = Form(None),  # todo: should we get this from auth?
    categories: Optional[str] = Form(None),
    images: Optional[list[UploadFile]] = File(None)
):
    # todo: upload image blobs to s3

    # todo: lookup and update post by post_id in db

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
