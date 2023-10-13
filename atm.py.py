import random as rn
for i in range(10):
    balance = str(rn.randrange(100000,300000))
    get1 = str(balance[0])
    get2 = str(balance[1])
    get3 = str(balance[2])


class user:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
    def balance(self):
        print('f')


while True:
    print("您好!請選擇以下功能")
    print("1.檢查餘額, 2.轉帳, 3.提款, 4.存入")
    action = str(input("請打入數字: "))

    if action != "1" or "2" or "3" or "4":
        while True:
            action = str(input("您輸入有誤，請重新打入數字: "))
            if action == "1" or "2" or "3" or "4":
                break
    