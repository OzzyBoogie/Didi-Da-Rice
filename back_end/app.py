from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/1')
def hello():  # put application's code here
    return 'Hello 1!'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000
    )
