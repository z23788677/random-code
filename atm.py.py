import random as rn
balance = (rn.randrange(10000,30000))

class user:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

uesr1 = user("吳翊晞", 22, balance)

def balance(self):
    print(user1.name,"您好!")
    print("你的銀行餘額為", +balance+ "USD")

def transport(self):
    acc = str(input("請輸入匯入帳戶，請讓帳戶至少12碼"))
    if len(acc) != 12:
        while True:
            acc = str(input("帳號輸入有誤，請重新輸入"))
            if len(acc) == 12:
                break
    tra_balance = int(input("你想匯出多少?: "))
    balance = balance - tra_balance

def outcome(self):
    balance()
    out = int(input("請問你要提領多少: "))
    balance = balance - out
    if out[2] and out[3] and out[4] != 0:
        print("本ATM提領1000為一個單位，請重新輸入")
        out = int(input("請問你要提領多少: "))
    print("您的餘額剩下: ", +balance)
    
while True:
    print("您好!請選擇以下功能")
    print("1.檢查餘額, 2.轉帳, 3.提款, 4.存入, 5.取出提款卡")
    action = str(input("請打入數字: "))

    if action != "1" or "2" or "3" or "4" or "5":
        while True:
            action = str(input("您輸入有誤，請重新打入數字: "))
            if action == "1" or "2" or "3" or "4" or "5":
                break
    if action == "1":
        balance()
    elif action == "2":
        transport()
    elif action == "3":
        outcome()
    elif action == "4":
        income()
    elif action == "5":
        print("歡迎你再次使用ATM")
        break
