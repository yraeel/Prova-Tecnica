from flask import Flask,jsonify, request, Response
import requests
import csv
import io


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




@app.route('/fields', methods=['GET'])
def get_fields():
    platform = request.args.get('platform')
    url = f"https://sidebar.stract.to/api/fields?platform={platform}"
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




@app.route('/<platform>', methods=['GET'])
def get_ads(platform):

    url_platform = f'https://sidebar.stract.to/api/fields?platform={platform}'
    url_accounts = f'https://sidebar.stract.to/api/accounts?platform={platform}'
    url_insights = f'https://sidebar.stract.to/api/insights?platform={platform}&account=account&token=token&fields=fields'
    headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
    }

    
    try:
        response = requests.get(url_platform, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        response_accounts = requests.get(url_accounts, headers=headers)
        response_accounts.raise_for_status()
        data_accounts = response_accounts.json()
        
        response_insights = requests.get(url_insights, headers=headers)
        response_insights.raise_for_status()
        data_insights = response_insights.json()


        # if "fields" in data:
        #     field_values = [field["value"] for field in data["fields"]]
        #     print("Valores dos campos:", field_values)  

        return jsonify(f'Platform {platform} Data: ', data, data_accounts, data_insights)
        
            
        # else:
        #     return jsonify({"error": "Resposta inesperada da API"}), 500
        

    

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Erro ao conectar à API: {str(e)}"}), 500


   

if __name__ == '__main__':
    app.run()


"""
iterar a lista de plataformas
e para cada plataforma iterar as contas de cada
e para cada conta iterar os insights
"""

"""

"""