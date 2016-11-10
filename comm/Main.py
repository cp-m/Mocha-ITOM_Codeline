# -*- encoding:utf-8 -*-
from tornado import web
#from plugins.linux import ssh
from Code_line import Code
from config.config import server as m
from config.config import test_server as t_m
from controllers.sqlinit import sqlinit

class Main(web.RequestHandler):
    def get(self):
        if self.get_cookie("auth", None) != '1':
            self.redirect("/logint.html")
        else:
            self.render("index.html")

class out(web.RequestHandler):
    def get(self):
        self.set_cookie('auth', '0')
        self.redirect('/logint.html')

class code_line(web.RequestHandler):
    def get(self):
        self.render("code_line.html")

class logint(web.RequestHandler):
    def get(self):
        self.render("logint.html")

    def post(self):
        """用户登录认证"""
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_auth=sqlinit().select_user
        pwd_auth=sqlinit().select_pwd
        if user_auth(username):
            sql_pwd = pwd_auth(user_auth(username)[0])[0][0]
            if password == sql_pwd:
                 self.set_cookie("auth", '1')
                 self.redirect("/ui.html")
            else:
                 print ("密码错误")
                 self.render("logint.html")
        else:
            user_auth="用户不存在"
            print (user_auth)
            self.render("logint.html")

class Uii(web.RequestHandler):
    def get(self, *args, **kwargs):
        obj_html = t_m.keys()
        up_text = ""
        sum = ""
        if self.get_cookie("auth", None) != '1':
            self.redirect("/logint.html")
        else:
            self.render("ui.html", obj_html=obj_html, up_text=up_text, sum=sum)

    def post(self):
        extra = self.get_argument("beiz", None)#备注
        projet = self.get_argument("projet", None)#项目名字
        mastet = self.get_argument("mastet", None)#更新的环境
        trunk = self.get_argument("trunk", None)#更新的分支
        #sum = "项目:"+projet+"。更新的分支:"+trunk+"。更新的环境:"+mastet
	sum="project:"+projet+"___branch:"+trunk+"___serverpath:"+mastet
        obj_html = t_m.keys()
        if projet and mastet and trunk:
            if mastet == 'test':
                """测试环境"""
                retu = Code.Code(cmd1="cd " + t_m[projet]["dir"], cmd2="/usr/bin/git fetch origin",
                                 cmd3="/usr/bin/git diff origin/" + trunk + " | diffstat", cmd4="/usr/bin/git checkout origin/" + trunk,
                                 ip=t_m[projet]["ip"], port=t_m[projet]["port"], username=t_m[projet]["username"],
                                 password=t_m[projet]["password"]).git_up()
                cmd = retu
            else:
                """正式环境"""
                #retu = Code.Code(cmd1="cd " + m[projet]["dir"], cmd2="git fetch origin", cmd3="git diff origin/"+trunk+" | diffstat",cmd4="git checkout origin/"+trunk, ip=m[projet]["ip"], port=m[projet]["port"], username=m[projet]["username"], password=m[projet]["password"]).git_up()
                retu = Code.Code(cmd1="cd " + m[projet]["dir"], cmd2="sudo /usr/bin/git fetch origin",
                                 cmd3="/usr/bin/git diff origin/" + trunk + " | diffstat", cmd4="/usr/bin/git checkout origin/" + trunk,
                                 ip=m[projet]["ip"], port=m[projet]["port"], username=m[projet]["username"],
                                 password=m[projet]["password"]).git_up()
                cmd = retu
        else:
            cmd="参数不足"
        #retu = Code.Code(cmd1="cd "+c["passport"]["dir"], cmd2="git diff origin/master | diffstat", cmd3="git checkout origin/master",ip=c["passport"]["ip"], port=c["passport"]["port"], username=c["passport"]["username"], password=c["passport"]["password"]).git_up()
        # a=Code.Code(cmd1="cd /home/zww/123", cmd2="pwd", ip=c["passport"]["ip"], port=c["passport"]["port"], username=c["passport"]["username"], password=c["passport"]["password"]).git_up()
        # if a:
        #     a=cmd
        #     print (cmd)
        self.render("ui.html", up_text=cmd, obj_html=obj_html, sum=sum)


class top(web.RequestHandler):
    def get(self,*args,**kwargs):
        a=ssh.linux
        f=a.linux('6','7')
        print (type(f))
        username=self.get_argument("username")
        IP = self.get_argument("IP")
        start_file_dir = self.get_argument("start_file_dir")
        awk_var = self.get_argument("awk_var")
        self.render("ui.html")
    # def post(self):
    #     name=self.get_argument("IP")
    #     username=self.get_argument("")
    #     print (name)
    #     self.render("ui.html")

class test(web.RedirectHandler):
    def get(self):
        # hub=ssh.linux('a','b')
        # print (hub)
        self.render("ui-elements.html")


