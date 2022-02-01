from be.api.v1.templates.nonAuthRoute import createNonAuthRouter
from fastapi import APIRouter


router = APIRouter(prefix="/users")


@router.get("")
async def root():
    return {"message": "Get Users from the users lambda!"}


@router.get("/{user_id}")
async def root(user_id):
    return {"id": user_id}


handler = createNonAuthRouter(router)
