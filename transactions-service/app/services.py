from app.models import Transaction
from app.config import ACCOUNT_API_URL  
from sanic.response import json
import aiohttp


class TransactionService:
    def __init__(self, db):
        self.collection = db['transactions']

    async def create_transaction(self, request):
        data = request.json
        transaction = Transaction.from_dict(data)

        async with aiohttp.ClientSession() as session:
            sender_response = await session.get(f"{ACCOUNT_API_URL}/accounts/{transaction.sender_cvu}")
            receiver_response = await session.get(f"{ACCOUNT_API_URL}/accounts/{transaction.receiver_cvu}")

            if sender_response.status != 200 or receiver_response.status != 200:
                return json({"status": "error", "message": "Sender or receiver account not found"}, status=404)

            sender_account = await sender_response.json()
            receiver_account = await receiver_response.json()

            if sender_account["data"]["balance"] < transaction.amount:
                return json({"status": "error", "message": "Insufficient balance"}, status=400)

            # Update balances
            sender_new_balance = sender_account["data"]["balance"] - transaction.amount
            receiver_new_balance = receiver_account["data"]["balance"] + transaction.amount

            await session.put(f"{ACCOUNT_API_URL}/accounts/{transaction.sender_cvu}", json={"balance": sender_new_balance})
            await session.put(f"{ACCOUNT_API_URL}/accounts/{transaction.receiver_cvu}", json={"balance": receiver_new_balance})

        result = await self.collection.insert_one(transaction.to_dict())
        return json({"status": "success", "data": {"id": str(result.inserted_id)}}, status=201)
    
    async def get_transactions_by_cvu(self, cvu):
        transactions = await self.collection.find({"$or": [{"sender_cvu": cvu}, {"receiver_cvu": cvu}]}).to_list(length=100)
        for transaction in transactions:
            del transaction["_id"]
        return json({"status": "success", "data": transactions}, status=200)