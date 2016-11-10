# -*- encoding:utf-8 -*-
from tornado import web

'''获取客户端get过来的监控参数'''

class zabbix(web.RequestHandler):

    def get(self,*args,**kwargs):
        mem=self.get_argument("mem")
        cpu=self.get_argument("cpu")
        print (mem,cpu)
        self.render("ui.html")


    def post(self):
        name=self.get_argument("IP")
        username=self.get_argument("")
