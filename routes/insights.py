from flask import Blueprint, request, jsonify
from services.api_client import fetch_data

insights_bp = Blueprint('insights', __name__)

@insights_bp.route('/insights', methods=['GET'])
def get_insights():
    platform = request.args.get('platform')
    account = request.args.get('account')
    fields = request.args.get('fields')
    token = request.args.get('token')

    url = f'https://sidebar.stract.to/api/insights?platform={platform}&account={account}&token={token}&fields={fields}'
    return jsonify(fetch_data(url))
