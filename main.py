from flask import Flask, jsonify, render_template, request
import os
import predictions

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        dados = [
            float(request.form['comp_sepala']),
            float(request.form['larg_sepala']),
            float(request.form['comp_petala']),
            float(request.form['larg_petala'])
        ]
        y_pred = predictions.predict(dados)
        return jsonify({"resultado" : y_pred})
    elif request.method == 'GET':
        return jsonify({"mensagem" : "Utilize o formulário"})




if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
