from fastapi.testclient import TestClient


def createTestClient(router):
    client = TestClient(router)
    return client
