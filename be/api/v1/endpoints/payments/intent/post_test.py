from utils.test_app import createTestClient
from be.api.v1.endpoints.payments.intent.post import router

client = createTestClient(router)

def test_post_payment_intent():
    req_body = {"amount": 200}
    response = client.post("/payments/intent", json=req_body)
    assert response.status_code == 200
    assert len(response.json().get('client_secret')) > 0
