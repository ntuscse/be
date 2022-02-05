from be.api.v1.templates.nonAuthRoute import createNonAuthRouter
from fastapi import APIRouter


router = APIRouter(prefix="/users")


@router.get("")
async def root():
    return {"users": [
        {"id": 1, "name": "Andrew"},
        {"id": 2, "name": "Benjamin"},
    ]}


@router.get("/{user_id}")
async def root(user_id):
    return {
        "id": user_id,
        "name": "Benjamin",
        "regTime": "1643716201"
    }


handler = createNonAuthRouter(router)
