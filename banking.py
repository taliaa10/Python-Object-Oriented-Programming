from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self, name, initialDeposit):
        return 0

    @abstractmethod
    def authenticate(self, name, accountNumber):
        return 0

    @abstractmethod
    def withdraw(self, withdrawalAmount):
        return 0

    @abstractmethod
    def deposit(self, depositAmount):
        return 0

    @abstractmethod
    def displayBalance(self):
        return 0


class SavingsAccount(Account):
    def __init__(self):
        #  {12345: ???}
        # [key][0] => name ; [key][1] => balance
        self.savingsAccount = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.savingsAccount[self.accountNumber] = [name, initialDeposit]
        print('Account creation has been successful. Your account number is ',
              self.accountNumber)

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0] == name:
                print('Authentication Successful!')
                self.accountNumber = accountNumber
                return True
            else:
                print('Authentication Failed')
                return False
        else:
            print('Authentication Failed')
            return False

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccount[self.accountNumber][1]:
            print('Insufficient Balance')
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawalAmount
            print('Withdrawal was successful.')
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount
        print('Desposit was successful.')
        self.displayBalance()

    def displayBalance(self):
        print('Available balance:', self.savingsAccount[self.accountNumber][1])


savingsAccount = SavingsAccount()
while True:
    print('Enter 1 to create a new account')
    print('Enter 2 to access to an existing account')
    print('Enter 3 to exit')
    userChoice = int(input())
    if userChoice is 1:
        print('Enter your name: ')
        name = input()
        print('Enter the initial deposit: ')
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
    elif userChoice is 2:
        print('Enter your name: ')
        name = input()
        print('Enter your account number: ')
        accountNumber = int(input())
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print('Enter 1 to withdraw')
                print('Enter 2 to deposit')
                print('Enter 3 to display available balance')
                print('Enter 4 to go back to the previous menu')
                userChoice = int(input())
                if userChoice is 1:
                    print('Enter a withdrawal amount: ')
                    withdrawalAmount = int(input())
                    savingsAccount.withdraw(withdrawalAmount)
                elif userChoice is 2:
                    print('Enter an amount to be deposited: ')
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingsAccount.displayBalance()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        quit()
