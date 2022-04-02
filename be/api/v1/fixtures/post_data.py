from datetime import datetime
from fastapi.encoders import jsonable_encoder
from be.api.v1.models.posts import Post, PostCategory

dummy_posts = [
    Post(id=1, title="post title1", body="this is some post content 1", author="John Doe",
         categories=[PostCategory.welfare], publishedDate=datetime.fromisoformat("2022-04-03T07:33:59.628909"), images=[]),
    Post(id=2, title="post title2", body="this is some post content 2", author="John Doe",
         categories=[PostCategory.welfare], publishedDate=datetime.fromisoformat("2022-04-03T07:33:59.628909"), images=[]),
    Post(id=3, title="post title3", body="this is some post content 3", author="John Doe",
         categories=[PostCategory.welfare], publishedDate=datetime.fromisoformat("2022-04-03T07:33:59.628909"), images=[]),
    Post(id=4, title="post title4", body="this is some post content 4", author="John Doe",
         categories=[PostCategory.welfare], publishedDate=datetime.fromisoformat("2022-04-03T07:33:59.628909"), images=[]),
    Post(id=5, title="post title5", body="this is some post content 5", author="John Doe",
         categories=[PostCategory.welfare], publishedDate=datetime.fromisoformat("2022-04-03T07:33:59.628909"), images=[]),
]

dummy_posts_json = []
for post in dummy_posts:
    dummy_posts_json.append(post.json(encoder=jsonable_encoder))
