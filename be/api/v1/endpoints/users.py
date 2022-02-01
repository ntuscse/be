from fastapi import APIRouter

router = APIRouter()


# parent route is /users/

@router.get("/")
async def root():
    return {"message": "Get Users!"}


@router.get("/user_id")
def read_item(user_id: int):
    table_name = os.environ.get('TABLE_NAME', '')
    table = boto3.resource(
        "dynamodb", region_name='us-west-2').Table(table_name)
    response = table.get_item(
        Key={
            'PK': user_id
        }
    )
    return {"user_obj": response['Item']}
