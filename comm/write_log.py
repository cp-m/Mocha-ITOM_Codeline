def wlog(args,args2,username,regip):
    a=os.path.split(os.path.realpath(__file__))[0]
    data = time.strftime("%y%m%d", time.localtime(time.time()))
    udata = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    username = username
    with open(a+'/'+'log'+'/'+data+ '.log','a+') as w:
        w.write('\nUser:%s IP:%s Update:%s Project:%s UpVersion:%s' %(username,regip,udata,args2,args))