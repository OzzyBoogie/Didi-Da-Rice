import pymysql

config_root = {'user': 'root',
               'password': '',
               'port': 3306,
               'host': '8.217.6.156',
               'db': 'DIDI-DA-RICE-USER-DB'}


class Mysql:

    def __init__(self):
        self.connection = pymysql.connect(host=config_root['host'],
                                          port=config_root['port'],
                                          user=config_root['user'],
                                          password=config_root['password'],
                                          db=config_root['db'])

    # 匹配一项
    def fetch_one_db(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchone()

    # 匹配所有
    def fetch_all_db(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    # 直接执行
    def exe_db(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
