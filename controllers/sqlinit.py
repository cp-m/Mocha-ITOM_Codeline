# -*- encoding:utf-8 -*-
from config.config import mysql_info
import MySQLdb

conn = MySQLdb.connect(host=mysql_info["ip"], port=int(mysql_info["port"]), user=mysql_info["user"],
                       passwd=mysql_info["pwd"], db=mysql_info["dbname"])
cursor = conn.cursor()

class sqlinit:
    def __init__(self):
        pass
    def select_user(self, username):
        """判断用户名是否存在"""
        SQL = ("SELECT username FROM logint WHERE username='%s'" % username)
        cursor.execute(SQL)
        user = cursor.fetchone()
        conn.commit()
        return user

    def select_pwd(self, username):
        """判断密码是否存在"""
        SQL = ("SELECT PASSWORD FROM logint WHERE username = '%s'" % username)
        cursor.execute(SQL)
        pdw = cursor.fetchall()
        conn.commit()
        return pdw
