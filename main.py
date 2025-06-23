from flask_cors import CORS
from flask import Flask, send_from_directory, request, jsonify

import calculator

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/styles/<css>')
def styles(css):
    return send_from_directory('styles', css)

@app.route('/scripts/<js>')
def scripts(js):
    return send_from_directory('scripts', js)

@app.route('/plus', methods=['POST', 'OPTIONS'])
def plus():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()

    data = request.get_json()
    try:
        result = calculator.plus(data['num1'], data['num2'])
        return jsonify({'result': result})
    except (KeyError, TypeError):
        return jsonify({'error': 'Неверные входные данные'}), 400

@app.route('/minus', methods=['POST', 'OPTIONS'])
def minus():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()

    data = request.get_json()
    try:
        result = calculator.minus(data['num1'], data['num2'])
        return jsonify({'result': result})
    except (KeyError, TypeError):
        return jsonify({'error': 'Неверные входные данные'}), 400

@app.route('/multiply', methods=['POST', 'OPTIONS'])
def multiply():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()

    data = request.get_json()
    try:
        result = calculator.mul(data['num1'], data['num2'])
        return jsonify({'result': result})
    except (KeyError, TypeError):
        return jsonify({'error': 'Неверные входные данные'}), 400

@app.route('/divide', methods=['POST', 'OPTIONS'])
def divide():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()

    data = request.get_json()
    try:
        result = calculator.div(data['num1'], data['num2'])
        return jsonify({'result': result})
    except (KeyError, TypeError):
        return jsonify({'error': 'Неверные входные данные'}), 400

def _build_cors_preflight_response():
    response = jsonify({'message': 'Preflight Request'})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response

def _corsify_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')