from fastapi import HTTPException
from fastapi.testclient import TestClient
from pytest import raises


def createTestClient(router):
    client = TestClient(router)
    return client


raisesHTTPException = raises(HTTPException)
