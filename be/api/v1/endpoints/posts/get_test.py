from utils.test_app import createTestClient, raisesHTTPException
from be.api.v1.endpoints.posts.get import router
from be.api.v1.fixtures.post_data import dummy_posts, dummy_posts_json


client = createTestClient(router)


def test_get_posts():
    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json() == [
        {'author': 'John Doe',
         'body': 'this is some post content 1',
         'categories': ['welfare'],
         'id': '1',
         'images': [],
         'publishedDate': '2022-04-03T07:33:59.628909',
         'title': 'post title1'},
        {'author': 'John Doe',
         'body': 'this is some post content 2',
         'categories': ['welfare'],
         'id': '2',
         'images': [],
         'publishedDate': '2022-04-03T07:33:59.628909',
         'title': 'post title2'},
        {'author': 'John Doe',
         'body': 'this is some post content 3',
         'categories': ['welfare'],
         'id': '3',
         'images': [],
         'publishedDate': '2022-04-03T07:33:59.628909',
         'title': 'post title3'},
        {'author': 'John Doe',
         'body': 'this is some post content 4',
         'categories': ['welfare'],
         'id': '4',
         'images': [],
         'publishedDate': '2022-04-03T07:33:59.628909',
         'title': 'post title4'},
        {'author': 'John Doe',
         'body': 'this is some post content 5',
         'categories': ['welfare'],
         'id': '5',
         'images': [],
         'publishedDate': '2022-04-03T07:33:59.628909',
         'title': 'post title5'},
    ]


def test_get_single_post_200():
    response = client.get("/posts/2")
    assert response.status_code == 200
    assert response.json() == {
        'author': 'John Doe',
        'body': 'this is some post content 2',
        'categories': ['welfare'],
        'id': '2',
        'images': [],
        'publishedDate': '2022-04-03T07:33:59.628909',
        'title': 'post title2',
    }


def test_get_single_post_404():
    with raisesHTTPException as err:
        client.get("/posts/6")
    assert err.value.status_code == 404
    assert err.value.detail == "Post not found"
