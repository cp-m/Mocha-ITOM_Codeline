# -*- encoding:utf-8 -*-
s_dir = '/data/apps/'
t_dir = '/data/apps/branches/'

server = {
"passport": {
    "password": '123',
    "port": "22", "username": "www",
    "ip": "127.0.0.1",
    "dir": s_dir+"www.baidu.com"},
"ucenter": (
    "10.25.12.107",
    s_dir + "www2.baidu.com"),
}

test_server = {
"passport": {
    "password": 'pwd',
    "port": "22", "username": "www",
    "ip": "127.0.0.1",
    "dir": t_dir+"www.baidu.com"},
"ucenter": (
    "127.0.0.1", t_dir + "www2.baidu.com"),
}#项目名称同步渲染到前端展示。

mysql_info = {
    "ip": "127.0.0.1",
    "user": "root",
    "pwd": "123",
    "port": "3306",
    "dbname": "codeline"
}
