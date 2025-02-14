from flask import Blueprint, jsonify
from services.api_client import fetch_data

platforms_bp = Blueprint('platforms', __name__)

@platforms_bp.route('/platforms', methods=['GET'])
def get_platforms():
    url = "https://sidebar.stract.to/api/platforms"
    return jsonify(fetch_data(url))