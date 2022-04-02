from utils.test_app import createTestClient, raisesHTTPException
from be.api.v1.endpoints.posts.get import router
from be.api.v1.fixtures.post_data import dummy_posts


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
    with raisesHTTPException as err:
        client.get("/posts/6")
    assert err.value.status_code == 404
    assert err.value.detail == "Post not found"
