# creating a bank account that contains the names of customers using various accounts and opens new account 
# for other ppl,which also allows deposit and withdrawal from its customers
# use command line argument to execute the program
import time
import random
customers = {}
savings_account = 12000
current_account = 20000
fullname = customers
originalamount = [current_account]

def pincode():
    return random.randrange(1111,9999)

def gen():
    return random.randrange(1111111111,9999999999)
    
accnumber = gen()
pin = pincode()

customers[accnumber]=[fullname,accnumber,pin]

def details():
    fullname = input('Enter your full name\n')
    accountnumber = int(input('Enter your account number\n'))
    pin = int(input('Enter your 4 digit pin number\n'))
    for accountnumber,pin in customers.items():
       if accountnumber == accnumber:
        if customers[2] == pin:
            check()
       else:
            print('Sorry! you have entered an invalid name or account number')
def retry():
    h = int(input('Which account do you want to deposit cash into\n1.Savings account\n2.Current account\n'))
    if h == 1:
        amount = int(input('Enter how much you want to deposit into your savings account\n'))
        l = (amount + savings_account)
        print('\nPlease wait while we process your request\n')
        time.sleep(2.0)
        print(f'You have successfully deposited {amount} and your account balance is {l}')
    elif h == 2:
        amount = int(input('Enter how much you want to deposit into your current account\n'))
        b = (amount + current_account)
        print('\nPlease wait while we process your request\n')
        time.sleep(2.0)
        print(f'You have successfully deposited {amount} and your account balance is {b}')
    else:
        print('Invalid selection number,Please retry')
        p = int(input('Would you like to\n1.Exit?\n2.Or go back to the previous page\n'))
        if p == 1:
            exit()
        elif p == 2:
            deposit()
        else:
            print('Invalid selection number')

def deposit():
    name = input('Enter your name\n')
    accountnumber =int(input('Enter your account number\n'))
    pin = int(input('Enter your 4 digit pin number\n'))
    for user_account_number,v in customers.items():
        if user_account_number == accnumber:
            if v[2] == pin:
                retry()
        else:
            print('Sorry! you have entered an invalid name or account number\nCreate a new account?\n')
            r = int(input('Do you want to continue?\n1.Yes\n2.No\n'))
            if r == 1:
                createacc()
            elif r == 2:
                p = int(input('Would you like to\n1.Exit?\n2.Or go back to the previous page\n'))
                if p == 1:
                    exit()
                elif p == 2:
                    deposit()
                else:
                    print('Invalid selection number')
            else:
                print('Invalid selection number,Please retry')

def redo():
    w = int(input('Which account do you want to withdraw cash from\n1.Savings account\n2.Current account\n'))
    if w == 1:
        amount = int(input('Enter the amount you want to withdraw'))
        e = (amount - savings_account)
        if e > savings_account:
            print('Please wait, while we process your request')
            time.sleep(2.0)
            print(f'You have successfully withdrawn {amount} from your account and your account balance is {e}')
        else:
            print('Insufficient balance')
    elif w == 2:
        amount = int(input('Enter the amount you want to withdraw'))
        d = (amount - current_account)
        if d > current_account:
            print('Please wait, while we process your request')
            time.sleep(2.0)
            print(f'You have successfully withdrawn {amount} from your account and your account balance is {d}')
        else:
            print('Insufficient balance')
    else:
        print('Invalid selection number,Please retry\n')
        p = int(input('Would you like to\n1.Exit?\n2.Or go back to the previous page\n'))
        if p == 1:
            exit()
        elif p == 2:
            withdraw()
        else:
            print('Invalid selection number')

def withdraw():
    name = input('Enter your name\n')
    accountnumber = int(input('Enter your account number\n'))
    pin = int(input('Enter your pin number\n'))
    for user_account_number,v in customers.items():
        if user_account_number == accnumber:
            if v[2] == pin:
                redo()
    else:
        print('Create new account\n')
        r = int(input('Do you want to continue?\n1.Yes\n2.No\n'))
        if r == 1:
            createacc()
        elif r == 2:
            p = int(input('Would you like to\n1.Exit?\n2.Or go back to the previous page\n'))
            if p == 1:
                exit()
            elif p == 2:
                withdraw()
            else:
                print('Invalid selection number')
        else:
            print('Invalid selection number,Please retry')


def createacc():
    fullname = input('\nEnter your full name\n')
    if len(fullname) > 1:
        pass
        email = input('\nEnter your email address\n')
        if '@gmail.com' in email:
            pass
            pin = int(input('\n**Make sure the 4 digit number you are gonna enter can be remembered to avoid complications while acessing your account**\nEnter a 4 digit number\n'))
            tel_number =input('\nEnter your mobile number\n')
            if len(tel_number) == 11:
                pass
                print('\nPlease wait, while we process your bank details\n')
                time.sleep(2.0)
                user_account_number = accnumber
                customers[user_account_number] = [fullname,email,pin,tel_number]
                g = (f'Dear {fullname} your account number is {accnumber}')
                print(g)
                customers[user_account_number].append(pin)	
                print('Now login with your details\n')
                login()
            else:
                print('\nIncorrect mobile number')
        else:
            print('\nInvalid email address')
    else:
        print('\nInvalid name')


def check():
    j = int(input('1.Savings account\n2.Current account\n'))
    details()
    if j == 1:
        print('Please wait, while we process your request')
        time.sleep(2.0)
        print(f'Your Savings bank account balance = {savings_account} ')
    elif j == 2:
        print('Please wait, while we process your request')
        time.sleep(2.0)
        print(f'Your Current bank account balance = {current_account}')
    else:
        print('Invalid selection number,Please retry')


def exit():
    p = int(input('Are you sure you want to exit\n1.Yes\n2.No\n'))
    if p == 1:
        print('Thanks for banking with us')
    else:
        opt()


def login():
    opt()


def opt():
    p = int(input('Do you want to\n1.Deposit cash?\n2.Withdraw cash?\n3.Check your account balance?\n4.Exit\n'))
    if p == 1:
        deposit()
    elif p == 2:
        withdraw()
    elif p == 3:
        check()
    elif p == 4:
        exit()
    else:
        print('Invalid selection number,Please retry') 




def bank():
    print('\nWelcome to Microfinance Bank\n')
    choice = int(input('Do you have an account with us\n1.Yes\n2.No\n'))
    if choice == 1:
        opt()
    elif choice == 2:
        createacc()
    else:
        print('Invalid selection number,Please retry\n')
bank()

