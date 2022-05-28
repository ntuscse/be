from fastapi import APIRouter
from be.api.v1.templates.non_auth_route import create_non_auth_router


router = APIRouter(prefix="/users")


@router.get("")
async def root():
    return {
        "users": [
            {"id": 1, "name": "Andrew"},
            {"id": 2, "name": "Benjamin"},
        ]
    }


@router.get("/{user_id}")
async def get_user_id(user_id):
    return {"id": user_id, "name": "Benjamin", "regTime": "1643716201"}


handler = create_non_auth_router(router)
