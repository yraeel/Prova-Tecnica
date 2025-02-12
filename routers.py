from flask import Flask, render_template, jsonify, request
import requests
app = Flask(__name__)

TOKEN = "ProcessoSeletivoStract2025"


@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "Nome": "Israel Machado",
        "Email": "israelmachado19@outlook.com",
        "Linkedin": "https://www.linkedin.com/in/israel-machado-954455181/",
        "GitHub": "https://github.com/yraeel"
    })


@app.route('/platforms', methods=['GET'])
def get_platforms():
    url = "https://sidebar.stract.to/api/platforms"

    headers = {
        "Authorization": f"Bearer {TOKEN}",  # Adiciona o token no cabeçalho
        "Content-Type": "application/json"   # Especifica que queremos JSON
    }

    try:
        # Faz a requisição GET com o token
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica se a resposta foi bem-sucedida (200 OK)

        data = response.json()  # Converte a resposta para JSON
        return jsonify(data)  # Retorna os dados para o cliente Flask
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Erro ao conectar à API: {str(e)}"}), 500


@app.route('/<platform>', methods=['GET'])
def get_ads_by_platform(platform):
    # Obtém as contas para a plataforma
    url_accounts = f"https://sidebar.stract.to/api/accounts?platform={platform}"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response_accounts = requests.get(url_accounts, headers=headers)
        response_accounts.raise_for_status()
        accounts_data = response_accounts.json()
        
        print(accounts_data)  # Verifique a estrutura da resposta
        
        all_ads = []
        
        # Verifique se a resposta contém uma chave 'accounts' ou ajuste conforme necessário
        if 'accounts' in accounts_data:
            accounts = accounts_data['accounts']
            # Para cada conta, buscamos os insights (anúncios)
            for account in accounts:
                account_name = account["name"]
                url_insights = f"https://sidebar.stract.to/api/insights?platform={platform}&account={account['id']}&token={TOKEN}&fields=ad_name,clicks,spend"

                response_insights = requests.get(url_insights, headers=headers)
                response_insights.raise_for_status()
                insights_data = response_insights.json()

                # Adiciona os anúncios à lista
                for ad in insights_data:
                    all_ads.append({
                        "platform": platform,
                        "ad_name": ad["ad_name"],
                        "clicks": ad["clicks"],
                        "spend": ad["spend"],
                        "account_name": account_name
                    })
        else:
            return jsonify({"error": "Estrutura de dados inesperada"}), 500
        
        # Converte os anúncios para CSV ou JSON
        return jsonify(all_ads)
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Erro ao conectar à API: {str(e)}"}), 500


@app.route('/accounts', methods=['GET'])
def get_accounts():
    platform = request.args.get('platform')
    url = f"https://sidebar.stract.to/api/accounts?platform={platform}"
    headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Erro ao conectar à API: {str(e)}"}), 500


@app.route('/insights', methods=['GET'])
def get_insights():
    platform = request.args.get('platform')
    account = request.args.get('account')
    fields = request.args.get('fields')
    token = request.args.get('token')
    url = f'https://sidebar.stract.to/api/insights?platform={platform}&account={account}&token={token}&fields={fields}'
    headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Erro ao conectar à API: {str(e)}"}), 500


if __name__ == '__main__':
    app.run()
