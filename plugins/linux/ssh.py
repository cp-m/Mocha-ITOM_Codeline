# -*- encoding:utf-8 -*-
import os
from tornado import web
class linux:
    def linux(start_time,end_time,user,ip,source_file,end_file):
        linux = os.popen('ssh -p 22 %s@%s' % (user, ip))
        return linux
 # #linux = os.popen('ssh -p 22 %s@%s %s update %s' %(user,s.server[b][0],pth,s.server[b][1]) )
 #    name=self.name
 #    return (name)