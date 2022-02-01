from fastapi import APIRouter

from .endpoints import users

router = APIRouter()


@router.get("/")
async def index():
    return {"api_version": "v1"}


router.include_router(users.router, prefix="/users", tags=["Users"])
