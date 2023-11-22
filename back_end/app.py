from flask import Flask, request
from flask_cors import CORS
from db import Mysql
import entity
import time

app = Flask(__name__)
cors = CORS(app)

mysql = Mysql()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=['POST'])
def login():
    data = request.form
    account = data.get('account')
    password = data.get('password')
    sql = "SELECT * FROM users WHERE user_name = '%s'" % account
    user_data = mysql.fetch_one_db(sql)

    if user_data is None:
        return {
            'message': 'User not found',
            'code': -1
        }
    user = entity.User(*user_data)  # 使用命名元组来表示用户对象

    stored_password = user.password
    # 这里需要使用适当的密码验证方法，例如哈希算法
    if password != stored_password:
        return {
            'message': 'Invalid password',
            'code': 1
        }

    # 登录成功，进行后续操作
    return {
        'message': 'Login successful',
        'account': user_data[0],
        'username': user_data[1],
        'fullname': user_data[3],
        'phone': user_data[4],
        'code': 0
    }


@app.route('/update_info', methods=['POST'])
def update_info():
    time.sleep(2)
    response = {
        'code': 400
    }
    return response


@app.route('/update_avatar', methods=['POST'])
def update_avatar():
    time.sleep(2)
    response = {
        'code': 400
    }
    return response


@app.route('/emit_order', methods=['POST'])
def emit_order():
    response = {
        'code': 400,
        'message': 'Success'
    }
    return response


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
