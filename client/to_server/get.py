# -*- encoding:utf-8 -*-
import requests

'''
客户端数据通过get传输到服务器端口
'''
ip='192.168.0.1'
time='12%3A01'

ret = requests.get('http://127.0.0.1:8888/zabbix?start_time=%s&username=www&IP=%s' %(time,ip))