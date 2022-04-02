from be.api.v1.endpoints.posts.post import router
from utils.test_app import createTestClient


client = createTestClient(router)


def test_post_post():
    response = client.post("/posts",
                           files=None,
                           data={
                               "title": "post titles are overrated",
                               "body": "post body is cool tho",
                               "author": "John Doe",
                           }
                           )
    assert response.status_code == 200
    assert response.json() == {
        'createdPost': {'author': 'John Doe',
                        'body': 'post body is cool tho',
                        'categories': None,
                        'id': '6',
                        'title': 'post titles are overrated'},
        'status': 'Post created successfully',
        'uploadedImages': [],
    }
