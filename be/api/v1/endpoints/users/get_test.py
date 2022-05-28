from utils.test_app import createTestClient
from be.api.v1.endpoints.users.get import router

client = createTestClient(router)


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == {
        "users": [{"id": 1, "name": "Andrew"}, {"id": 2, "name": "Benjamin"}]
    }


def test_get_user():
    response = client.get("/users/2")
    assert response.status_code == 200
    assert response.json() == {"id": "2", "name": "Benjamin", "regTime": "1643716201"}
