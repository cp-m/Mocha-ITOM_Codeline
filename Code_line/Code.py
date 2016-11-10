# -*- encoding:utf-8 -*-
#from config.config import server as c
# from config import server as c
class Code:
    def __init__(self, username, port, password, ip, cmd1, cmd2, cmd3, cmd4):
        self.name = username
        self.port = port
        self.password = password
        self.ip = ip
        self.cmd1 = cmd1
        self.cmd2 = cmd2
        self.cmd3 = cmd3
        self.cmd4 = cmd4

    def git_up(self):
        """git代码更新"""
        import paramiko
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip, int(self.port), self.name, self.password)
            stdin, stdout, stderr = ssh.exec_command(self.cmd1+";"+self.cmd2+";"+self.cmd3+";"+self.cmd4)
            return stdout.read()
        except :
            return "更新失败，请检查配置"
        ssh.close()


        # linux = ''
        # if c.isdigit():
        #    os.popen('ssh -p 22 %s@%s %s revert -R %s' %(user,s.server[b][0],pth,s.server[b][1]) )
        #    linux = os.popen('ssh -p 22 %s@%s %s update -r%s %s' %(user,s.server[b][0],pth,c,s.server[b][1]) )
        #    wlog(c,b,username,regip)
        # elif c == 'up':
        #    os.popen('ssh -p 22 %s@%s %s revert -R %s' %(user,s.server[b][0],pth,s.server[b][1]) )
        #    linux = os.popen('ssh -p 22 %s@%s %s update %s' %(user,s.server[b][0],pth,s.server[b][1]) )
        #    wlog('update',b,username,regip)
        # else:
        #    linux = 'Input error'
        # return linux
#Code().git_up()
#Code(cmd1="cd /home/zww/123", cmd2="pwd", ip=c["passport"]["ip"], port=c["passport"]["port"], username=c["passport"]["username"], password=c["passport"]["password"]).git_up()