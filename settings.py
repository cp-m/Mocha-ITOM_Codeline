# -*- encoding:utf-8 -*-
import sys
import os
sys.path.append(os.getcwd())
import tornado.ioloop
from tornado import web
from comm.Main import Uii
from comm.Main import top
from comm.Main import test
from comm.zabbix import zabbix
from comm.obtain import obtain
from comm.Main import code_line
from comm.Main import Main
from comm.Main import out
from comm.Main import logint

settings = {
    'template_path': 'tmp',
    'static_path': 'static',
}
application = tornado.web.Application([
    (r"/index", Main),
    (r"/index.html", Main),
    (r"/ui.html", Uii),
    (r"/out", out),
    (r"/logint.html", logint),
    (r"/zabbix.html", zabbix),
    (r"/top*", top),
    (r"/*", Main),
    (r"/obtain", obtain),
    (r"/test*", test),
    (r"/Code_line", code_line),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
