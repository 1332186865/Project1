# 编写代码,验证密码的合法性,具体标准如下:
# 若密码长度小于6,或者超过16,或者密码包含除了数字、字母以及"._?!@"之外的符号,全部判断为非法密码。

def password_truth(password):
    flag = 1
    if len(password) < 6 or len(password) > 16:
        flag = 0
    for i in password:
        if i.isdigit() and i.isalpha() and i not in '._?!@':
            flag = 0
    return flag


if __name__ == '__main__':
    password = input('请输入密码')
    if password_truth(password):
        print('有效密码')
    else:
        print('非法密码')
