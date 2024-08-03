from app.models import Account
from sanic.response import json


class AccountService:
    def __init__(self, db):
        self.collection = db['accounts']

    async def create_account(self, request):
        data = request.json
        account = Account.from_dict(data)
        # validate if account with that cvu value already exists
        existing_account = await self.collection.find_one({"cvu": account.cvu})
        if existing_account:
            return json({"status": "error", "message": "Account with that CVU already exists"}, status = 409)
        else:
            result = await self.collection.insert_one(account.to_dict())
            return json({"status": "success", "data": {"id": str(result.inserted_id)}}, status=201)
    
    async def get_account_by_cvu(self, account_cvu):
        account = await self.collection.find_one({"cvu": account_cvu})
        if account:
            del account["_id"]
            return json({"status": "success", "data": account}, status = 200)
        else:
            return json({"status": "error", "message": "Account not found"}, status = 404)
        
    async def update_account_by_cvu(self, account_cvu, data):
        result = await self.collection.update_one({"cvu": account_cvu}, {"$set": data})
        if result.matched_count:
            updated_account = await self.collection.find_one({"cvu": account_cvu})
            del updated_account["_id"]
            return json({"status": "success", "data": updated_account}, status=200)
        else:
            return json({"status": "error", "message": "Account not found"}, status = 404)
        
    async def delete_account_by_cvu(self, account_cvu):
        result = await self.collection.delete_one({"cvu": account_cvu})
        if result.deleted_count:
            return json({"status": "success", "message": "Account deleted"}, status=200)
        else:
            return json({"status": "error", "message": "Account not found"}, status = 404)