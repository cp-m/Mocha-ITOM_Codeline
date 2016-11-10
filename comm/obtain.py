# -*- encoding:utf-8 -*-
from tornado import web
class obtain(web.RequestHandler):
    def get(self):
        with open('G:/python作业/Mocha-ITOM/comm/a.txt', 'r',encoding='utf-8') as f:
            b=f.read()
        with open('G:/python作业/Mocha-ITOM/comm/cpu.txt', 'r', encoding='utf-8') as c:
            c = c.read()
        self.render("2.html",list_info = b,cpu=c)
