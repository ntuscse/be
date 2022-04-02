from turtle import pos
from utils.test_app import createTestClient
from be.api.v1.endpoints.posts.get import router, dummy_posts

client = createTestClient(router)


def test_get_posts():
    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json() == dummy_posts


def test_get_single_post_200():
    response = client.get("/posts/2")
    assert response.status_code == 200
    assert response.json() == dummy_posts[1]


def test_get_single_post_404():
    response = client.get("/posts/6")
    assert response.status_code == 404
    # todo: assert the 404 detail msg
