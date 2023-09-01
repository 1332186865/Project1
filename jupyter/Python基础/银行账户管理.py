class BankAccount(object):
    """模拟银行账户的用户管理、密码验证、进账等操作
    >>>b = BankAccount('Bart',111)
    >>>b.__add_rules()
    >>>b.__add_rules()
    transaction failed
    >>>b.display()
    Bart, 100
    """

    def __init__(self, name, pwd):  # 用户信息初始化，包括用户名、密码、初始余额
        # input your code
        self.name = name
        self.pwd = pwd
        self.money = 0

    def _authenticate(self, pwd):  # 验证密码是否正确
        # input your code
        if self.name == 'Bark':
            if pwd == 111:
                return True
            else:
                return False
        else:
            return False

    def add(self, amount, pwd):  # 入账
        if pwd == self.pwd:
            self.money += amount
            print('finished')
            return
        else:
            print('transaction failed')

    def display(self):  # 显示当前账户信息及余额
        # input your code
        return "{} {}".format(self.name, self.pwd)


b = BankAccount('Bart', 111)
b.add(100, 111)
b.add(200, 222)
print(b.display())
