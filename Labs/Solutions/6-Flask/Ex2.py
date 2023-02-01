from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f'Hello, {name}!'


@app.route('/greet', methods=['POST'])
def greet_post():
    data = request.get_json()
    name = data['name']
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run()
