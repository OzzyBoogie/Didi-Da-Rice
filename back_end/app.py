from flask import Flask, request
from flask_cors import CORS
from flask_mysqldb import MySQL
import entity
import time

# from collections import namedtuple

# # 定义命名元组的结构(用户账号数据库)
# User = namedtuple('User', ['id', 'username', 'password', 'fullname', 'phone'])

app = Flask(__name__)
cors = CORS(app)

# Required
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "DIDI-DA-RICE-USER-DB"
# Extra configs, optional:
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}  # https://mysqlclient.readthedocs.io/user_guide.html#functions-and-attributes

mysql = MySQL(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=['POST'])
def login():
    data = request.form
    account = data.get('account')
    password = data.get('password')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (account,))
    user_data = cur.fetchone()

    if user_data is None:
        # print(-1)
        return {
            'message': 'User not found',
            'code': -1
        }
    user = entity.User(*user_data)  # 使用命名元组来表示用户对象

    stored_password = user.password
    # 这里需要使用适当的密码验证方法，例如哈希算法
    if password != stored_password:
        # print(1)
        return {
            'message': 'Invalid password',
            'code': 1
        }

    # 登录成功，进行后续操作
    # print(0)
    return {
        'message': 'Login successful',
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
