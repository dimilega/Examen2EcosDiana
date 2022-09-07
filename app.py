from model import model_lr
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "<h1>Regréssion linéaire simple</h1>"

@app.route('/fit', methods=['GET'])
def fit():
    response = {'parameters': model_lr}

    return response


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    y = data['x0'] * model_lr['theta0'] + data['x1'] * model_lr[
        'theta1'] + data['x2'] * model_lr['theta2']

    response = {'y': y}

    return response


if __name__ == '__main__':
    app.run()
