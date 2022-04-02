from be.api.v1.endpoints.posts.patch import router
from utils.test_app import createTestClient


client = createTestClient(router)


def test_patch_post():
    response = client.patch("/posts/2",
                            files=None,
                            data={}
                            )
    assert response.status_code == 200
    assert response.json() == {
        'status': 'Post created successfully',
        'update': [None],
        'updatedPost': {'author': None,
                        'body': None,
                        'categories': None,
                        'id': '2',
                        'title': None},
    }
