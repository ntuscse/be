
from be.api.v1.templates.nonAuthRoute import createNonAuthRouter
from fastapi import APIRouter


router = APIRouter(prefix="/users")


@router.get("")
async def root():
    return {"message": "Get Users from the users lambda!"}


handler = createNonAuthRouter(router)
