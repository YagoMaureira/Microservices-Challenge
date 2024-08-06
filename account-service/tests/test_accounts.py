from app.app_factory import create_app
import pytest


@pytest.fixture
def app():
    return create_app()

def test_create_account(app):
    _, response = app.test_client.post("/accounts", json={
        "cvu": "1234567891011121314789",
        "username": "test",
        "email": "test@example.com",
        "balance": 1000.0
    })

    assert response.status == 201

def test_get_account_by_cvu(app):
    _, response = app.test_client.get("/accounts/1234567891011121314789")

    assert response.status == 200

def test_update_account(app):
    _, response = app.test_client.put("/accounts/1234567891011121314789", json={
        "balance": 2000.0
    })

    assert response.status == 200

def test_delete_account(app):
    _, response = app.test_client.delete("/accounts/1234567891011121314789")

    assert response.status == 200
