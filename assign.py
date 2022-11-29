# create more tnan one functions that contains the day to day activities in a bank
# i.e:how to create a bank account,how to deposit money,how to withdraw money.

import time
import random 
accounts = {'amarachi':2334498760}
accountnumber = [3474677401,8346957402,8399023490,7886552377,7049352410]

def createacc(l):
    name = input('enter your name\n')
    if len(name)>=1:
        pass
        email = input('enter your email address\n')
        if '@gmail.com' in email:
            pass
            age = int(input('enter your age\n'))
            if  age >= 18:
                pass
                tele = input('enter your mobile number\n')
                if len(tele) == 11:
                    pass
                    print('processing your bank details')
                    time.sleep(0.10)
                    t = random.choice(accountnumber)
                    print(f'your account number is {t}')
                    accounts[name] = t
                else:
                    print('invalid telephone number')
            else:
                print('your age does not qualify you to use a current account')
        else:
            print('invalid email address')
    else:
        print('invalid name')


def deposit(myacc):
    x = input('enter your name\n')
    if x in accounts:
        acc = int(input('enter your account number\n'))
        if len(str(acc)) == 10:
            firstamount = int(input('enter amount to be deposited\n'))
            time.sleep(5.0)
            print(f'amount deposited - N{firstamount}')
        else:
            print('invalid account number')
    else :
        print('create new account\n')        
        d = int(input('do you want to continue\n1.yes\n2.no\n'))
        if d == 1:
            createacc('l')    
        else:
            print('thanks for banking with us')         


def withdraw(myacc):
    amount = int(amount)
    secondamount = int(input('enter amount to be withdrawn:'))
    if amount + 500 >= secondamount:
        balance = amount-secondamount
        print(f'you have credited you N{balance} from your account')
    else:
        print('insufficient balance')


def account(name):
    choice = int(input('1.create account\n2.deposit or\n3.withdrawal\n'))
    if choice == 1:
        createacc('l')
    elif choice == 2:
        deposit('myacc')
    elif choice == 3:
        withdraw('myacc')
account('name')










