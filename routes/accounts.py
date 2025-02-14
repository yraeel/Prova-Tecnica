from flask import Blueprint, request, jsonify
from services.api_client import fetch_data

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/accounts', methods=['GET'])
def get_accounts():
    platform = request.args.get('platform')
    url = f"https://sidebar.stract.to/api/accounts?platform={platform}"
    return jsonify(fetch_data(url))
