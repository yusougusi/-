from time import sleep
from random import randint
import threading
from concurrent.futures import ThreadPoolExecutor


class Account():
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        lock = threading.Lock()
        self.condition = threading.Condition(lock)

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def despoit(self, money):
        """春浅"""
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()

def add_money(account):
    money = randint(5, 10)
    account.despoit(money)
    print(threading.current_thread().name, ':', money, '=====>', account.balance)
    sleep(0.5)


def sub_money(account):
    money = randint(10, 20)
    account.withdraw(money)
    print(threading.current_thread().name,':', money, '<====', account.balance)
    sleep(1)


def main():
    accont = Account()
    with ThreadPoolExecutor(max_workers=15) as pool:
        for _ in range(10):
            pool.submit(add_money, accont)
        for _ in range(5):
            pool.submit(sub_money, accont)


if __name__ == '__main__':
    main()
