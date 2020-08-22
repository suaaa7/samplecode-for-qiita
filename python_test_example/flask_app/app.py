import json

from flask import Flask, jsonify, make_response
from flask.wrappers import Response

from .service import Service

app = Flask(__name__)

print('Instantiate Service in app')
service = Service()

@app.route('/', methods=['GET'])
def index() -> Response:
    message = {'message': 'OK'}
    return make_response(jsonify(message), 200)

@app.route('/predict', methods=['POST'])
def predict() -> Response:
    print('Call predict in app')
    target = 'A'
    if not service.check_model():
        return make_response(jsonify({'message': 'Service Unavailable'}), 503)
    result = {'result': service.predict(target)}
    return make_response(jsonify(result), 200)
