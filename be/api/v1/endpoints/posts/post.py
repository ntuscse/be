from types import NoneType
from typing import Optional
from fastapi import APIRouter, File, Form, UploadFile

from be.api.v1.templates.authRoute import createAuthRouter
from be.api.v1.fixtures.post_data import dummy_posts

router = APIRouter(prefix="/posts")


@router.post("")
async def post_posts(
    title: str = Form(...),
    body: str = Form(...),
    author: str = Form(...),  # todo: should we get this from auth?
    categories: Optional[str] = Form(None),
    images: Optional[list[UploadFile]] = File(None)
):
    # todo: upload image blobs to s3
    images_filenames = []
    if type(images) != NoneType:
        for image in images:
            images_filenames.append(image.filename)

    new_id = str(int(dummy_posts[-1]["id"])+1)

    return {
        "status": "Post created successfully",
        "uploadedImages": images_filenames,
        "createdPost": {
            "id": new_id,
            "title": title,
            "body": body,
            "author": author,
            "categories": categories,
        }
    }

handler = createAuthRouter(router)
