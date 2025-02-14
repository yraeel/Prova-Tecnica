
from flask import Flask, jsonify
from routes.platforms import platforms_bp
from routes.accounts import accounts_bp
from routes.insights import insights_bp
from routes.ads import ads_bp

app = Flask(__name__)


app.register_blueprint(platforms_bp)
app.register_blueprint(accounts_bp)
app.register_blueprint(insights_bp)
app.register_blueprint(ads_bp)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "Nome": "Israel Machado",
        "Email": "israelmachado19@outlook.com",
        "Linkedin": "https://www.linkedin.com/in/israel-machado-954455181/",
        "GitHub": "https://github.com/yraeel"
    })


if __name__ == '__main__':
    app.run(debug=True)