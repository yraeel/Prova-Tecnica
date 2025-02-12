from flask import Flask, render_template, jsonify, request
import requests
app = Flask(__name__)

TOKEN = "ProcessoSeletivoStract2025"


@app.route('/', methods=['GET'])
def root():
    return render_template('geral.html')


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


@app.route('/get_fields', methods=['GET'])
def get_fields():
    platform = request.args.get('platform')
    url = f"https://sidebar.stract.to/api/fields?platform={platform}"
    headers = {
        "Authorization": f"Bearer {TOKEN}",  # Adiciona o token no cabeçalho
        "Content-Type": "application/json"   # Especifica que queremos JSON
    }

    try:
        # Faz a requisição GET para pegar os "fields"
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica se a resposta foi bem-sucedida (200 OK)

        data = response.json()  # Converte a resposta para JSON
        # Retorna os dados dos "fields" para o cliente Flask
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Erro ao conectar à API: {str(e)}"}), 500


if __name__ == '__main__':
    app.run()
