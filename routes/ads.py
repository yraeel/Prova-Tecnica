from flask import Blueprint, request, jsonify
from services.api_client import fetch_data

ads_bp = Blueprint('ads', __name__)

@ads_bp.route('/<platform>', methods=['GET'])
def get_ads(platform):
    url_platform = f'https://sidebar.stract.to/api/fields?platform={platform}'
    url_accounts = f'https://sidebar.stract.to/api/accounts?platform={platform}'

    data_platform = fetch_data(url_platform)
    available_fields = [field["value"] for field in data_platform.get("fields", [])]
    fields_param = request.args.get("fields", ",".join(available_fields))

    data_accounts = fetch_data(url_accounts)
    accounts_list = data_accounts.get("accounts", [])
    insights_data = []

    for account in accounts_list:
        account_id = account.get("id")
        account_token = account.get("token")

        if account_id and account_token:
            url_insights = f'https://sidebar.stract.to/api/insights?platform={platform}&account={account_id}&token={account_token}&fields={fields_param}'
            insights_data.append({
                "account_id": account_id,
                "account_name": account.get("name"),
                "insights": fetch_data(url_insights)
            })

    return jsonify({
        "platform": platform,
        "data_platform": data_platform,
        "accounts": accounts_list,
        "insights": insights_data
    })
