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
        return jsonify({
            "setosa" : f'{y_pred[0]}',
            "versicolor" : f'{y_pred[1]}',
            "virginica" : f'{y_pred[2]}'
        })
    elif request.method == 'GET':
        return jsonify({"mensagem" : "Utilize o formulário"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

#- para rodar localmente
# pip install flask
# pip install torch numpy torchvision
# flask --app main run