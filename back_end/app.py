from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=['POST'])
def login(): 
    data=request.form
    account = data.get('account')
    password = data.get('password')
    if account =='admin' and password=='123456':
        return {
            'message': 'Login OK',
            'code': 1
            }
    return 'Fail'

@app.route('/api/post', methods=['POST'])
def handle_post_request():
    data = request  # 获取POST请求的JSON数据
    # 处理数据...
    response = {'message': 'Success'}
    return response, 200  # 返回JSON响应和状态码

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000
    )
