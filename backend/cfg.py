from flask_mysqldb import MySQL

class Config(object):
    def __init__(self):
        self.MYSQL_HOST = "35.202.223.234"
        self.MYSQL_USER = "root"
        self.MYSQL_PASSWORD = "15441109"
        self.MYSQL_DB = "apitool_test"
        