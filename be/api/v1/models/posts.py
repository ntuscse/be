from datetime import datetime
from enum import Enum
from pydantic import HttpUrl, BaseModel, constr


class PostCategory(str, Enum):
    merch = 'merch'
    exams = 'exams'
    welfare = 'welfare'


class Post(BaseModel):
    id: str
    title: constr(max_length=49)
    body: str
    author: constr(max_length=49)
    categories: list[PostCategory]
    images: list[HttpUrl]
    publishedDate: datetime
