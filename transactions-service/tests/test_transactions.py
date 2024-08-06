from dotenv import load_dotenv
from sanic import Sanic
from app.routes import setup_routes
from app.utils import init_db
import pytest
import os


@pytest.fixture
def app():
    load_dotenv()

    Sanic.test_mode = True
    sanic_app = Sanic("sanic-test")

    sanic_app.config.update({
        "MONGO_URI": os.getenv("MONGO_URI"),
        "ACCOUNT_API_URL": os.getenv("ACCOUNT_API_URL")
    })

    setup_routes(sanic_app)
    init_db(sanic_app)
    return sanic_app


def test_create_transfer(app):
    # Making the request to create a transfer
    _, response = app.test_client.post("/transactions", json={
        "sender_cvu": "1234567891011121314456",
        "receiver_cvu": "1234567891011121314151",
        "amount": 100
    })

    assert response.status == 201


def test_get_transactions_by_cvu(app):
    _, response = app.test_client.get("/transactions/cvu/1234567891011121314456")

    assert response.status == 200
