from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"mensagem": "Bom dia André Luiz Franca Batista"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
