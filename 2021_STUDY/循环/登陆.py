i = 0
# 默认用户名：Admin 默认密码：admin
defaultLogin = "Admin"
defaultPasswd = "admin"
while i < 3:
    login = input("请输入用户名：")
    passwd = input("请输入密码")
    if login == defaultLogin and passwd == defaultPasswd:
        print("登陆成功")
        break
    elif login != defaultLogin:
        print("用户名错误！")
    elif passwd != defaultPasswd:
        print("密码错误！")
    i += 1
else:
    print("登陆机会已用尽")
