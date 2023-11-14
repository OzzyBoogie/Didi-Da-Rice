from collections import namedtuple

# 定义命名元组的结构(用户账号数据库)
User = namedtuple('User', ['id', 'username', 'password', 'fullname', 'phone'])
