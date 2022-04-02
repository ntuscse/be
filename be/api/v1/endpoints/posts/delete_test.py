from be.api.v1.endpoints.posts.delete import router
from utils.test_app import createTestClient, raisesHTTPException


client = createTestClient(router)


def test_delete_post():
    response = client.delete("/posts/2")
    assert response.status_code == 200
    assert response.json() == {'status': 'Post deleted successfully'}


def test_delete_post_nonexistent():
    with raisesHTTPException as err:
        client.delete("/posts/6")
    assert err.value.status_code == 204
    assert err.value.detail == "Post not found"
