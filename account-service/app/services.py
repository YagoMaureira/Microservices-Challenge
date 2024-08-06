from app.models import Account
from sanic.response import json


class AccountService:
    def __init__(self, db):
        self.collection = db['accounts']

    async def create_account(self, request):
        data = request.json
        account = Account.from_dict(data)

        #validate if the cvu is a string, have 22 numerical characters and not empty
        if not isinstance(account.cvu, str) or not account.cvu or not account.cvu.isnumeric() or len(account.cvu) != 22:
            return json({"status": "error", "message": "CVU must be a string with 22 numerical characters and not empty"}, status = 400)
        
        # validate if username and email value is string and not empty
        if not isinstance(account.username, str) or not isinstance(account.email, str) or not account.username or not account.email:
            return json({"status": "error", "message": "Username and email must be strings and not empty"}, status = 400)
        
        # validate if balance value is a float and not empty
        if not isinstance(account.balance, float) or not account.balance:
            return json({"status": "error", "message": "Balance must be a float and not empty"}, status = 400)
        
        # validate if account with that cvu value already exists
        existing_account = await self.collection.find_one({"cvu": account.cvu})
        if existing_account:
            return json({"status": "error", "message": "Account with that CVU already exists"}, status = 409)
        
        result = await self.collection.insert_one(account.to_dict())
        return json({"status": "success", "data": {"id": str(result.inserted_id)}}, status=201)
    
    async def get_account_by_cvu(self, account_cvu):

        #validate if the cvu is a string, have 22 numerical characters and not empty
        if not isinstance(account_cvu, str) or not account_cvu or not account_cvu.isnumeric() or len(account_cvu) != 22:
            return json({"status": "error", "message": "CVU must be a string with 22 numerical characters and not empty"}, status = 400)
        
        account = await self.collection.find_one({"cvu": account_cvu})
        if account:
            del account["_id"]
            return json({"status": "success", "data": account}, status = 200)
        else:
            return json({"status": "error", "message": "Account not found"}, status = 404)
        
    async def update_account_by_cvu(self, account_cvu, data):

        #validate if the cvu is a string, have 22 numerical characters and not empty
        if not isinstance(account_cvu, str) or not account_cvu or not account_cvu.isnumeric() or len(account_cvu) != 22:
            return json({"status": "error", "message": "CVU must be a string with 22 numerical characters and not empty"}, status = 400)

        result = await self.collection.update_one({"cvu": account_cvu}, {"$set": data})
        if result.matched_count:
            updated_account = await self.collection.find_one({"cvu": account_cvu})
            del updated_account["_id"]
            return json({"status": "success", "data": updated_account}, status=200)
        else:
            return json({"status": "error", "message": "Account not found"}, status = 404)
        
    async def delete_account_by_cvu(self, account_cvu):

        #validate if the cvu is a string, have 22 numerical characters and not empty
        if not isinstance(account_cvu, str) or not account_cvu or not account_cvu.isnumeric() or len(account_cvu) != 22:
            return json({"status": "error", "message": "CVU must be a string with 22 numerical characters and not empty"}, status = 400)

        result = await self.collection.delete_one({"cvu": account_cvu})
        if result.deleted_count:
            return json({"status": "success", "message": "Account deleted"}, status=200)
        else:
            return json({"status": "error", "message": "Account not found"}, status = 404)
        