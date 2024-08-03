from sanic import Blueprint
from app.services import AccountService


accounts_bp = Blueprint("accounts")


@accounts_bp.route('/accounts', methods=['POST'])
async def create_account(request):
    service = AccountService(request.app.ctx.db)
    return await service.create_account(request)

@accounts_bp.route('/accounts/<account_cvu>', methods=['GET'])
async def get_account(request, account_cvu):
    service = AccountService(request.app.ctx.db)
    return await service.get_account_by_cvu(account_cvu)

@accounts_bp.route('/accounts/<account_cvu>', methods=['PUT'])
async def update_account(request, account_cvu):
    service = AccountService(request.app.ctx.db)
    return await service.update_account_by_cvu(account_cvu, request.json)

@accounts_bp.route('/accounts/<account_cvu>', methods=['DELETE'])
async def delete_account_by(request, account_cvu):
    service = AccountService(request.app.ctx.db)
    return await service.delete_account_by_cvu(account_cvu)

def setup_routes(app):
    app.blueprint(accounts_bp)