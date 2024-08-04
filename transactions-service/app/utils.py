from motor.motor_asyncio import AsyncIOMotorClient


def init_db(app):
    app.ctx.db = AsyncIOMotorClient(app.config.MONGO_URI).get_database('transactions-service')