from sanic import Sanic
from app.routes import setup_routes
from app.utils import init_db
from dotenv import load_dotenv
import app.config as config


def create_app() -> Sanic:
    load_dotenv()
    app = Sanic("transactions-service")

    app.config.update({
        "MONGO_URI": config.MONGO_URI,
        "ACCOUNT_API_URL": config.ACCOUNT_API_URL
    })

    setup_routes(app)
    init_db(app)
    return app