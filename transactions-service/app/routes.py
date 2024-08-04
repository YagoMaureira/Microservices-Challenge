from sanic import Blueprint
from app.services import TransactionService

transactions_bp = Blueprint("transactions")


@transactions_bp.route("/transactions", methods=["POST"])
async def create_transaction(request):
    service = TransactionService(request.app.ctx.db)
    return await service.create_transaction(request)

@transactions_bp.route('/transactions/cvu/<cvu>', methods=['GET'])
async def get_transactions_by_cvu(request, cvu):
    service = TransactionService(request.app.ctx.db)
    return await service.get_transactions_by_cvu(cvu)

def setup_routes(app):
    app.blueprint(transactions_bp)