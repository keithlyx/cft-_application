from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/add', methods=['POST'])
def add():
    try:
        print(request.form)
        num1 = float(request.form.get('num1', 0))
        num2 = float(request.form.get('num2', 0))
        result = num1 + num2
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/subtract', methods=['POST'])
def subtract():
    try:
        num1 = float(request.form.get('num1', 0))
        num2 = float(request.form.get('num2', 0))
        result = num1 - num2
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(port=3000)
