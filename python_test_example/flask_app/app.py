import json

from flask import Flask, jsonify

from .service import Service

app = Flask(__name__)

print('Instantiate Service in app')
service = Service()

@app.route('/', methods=['GET'])
def index():
    message = {'Message': 'ok'}
    return jsonify(message)

@app.route('/predict', methods=['POST'])
def predict():
    print('Call predict in app')
    target = 'A'
    message = {'result': service.predict(target)}
    return jsonify(message)
