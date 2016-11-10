# -*- encoding:utf-8 -*-
import os
import sys
import time
from plugins.linux import *
from plugins.windows import pcinfo
import requests
from config import config
sys.path.append(os.getcwd())

'''启动'''

while True:
    time.sleep(5)
    cpu=pcinfo.cpu()
    mem=pcinfo.mem()
    ret = requests.get('http://$s:8888/zabbix.html?mem=%s&cpu=%s' % (config.serverip,mem, cpu))





