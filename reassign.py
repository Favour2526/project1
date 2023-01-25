# creating a bank account that contains the names of customers using various accounts and opens new account 
# for other ppl,which also allows deposit and withdrawal from its customers
import sqlite3
import time
import random

class Bank():
    customers = {}
    savings_account = [0.0]
    current_account = [0.0]

    def __init__(self):
        super().__init__()
        self.bank()
        self.createacc()
        self.options()
        self.gen()
        self.login()
        self.deposit2()
        self.deposit()
        self.withdraw2()
        self.withdraw()
        self.check()
        self.exit()
        
    def gen(self):
        accnumber = random.randrange(1111111111,9999999999)
        return random.randrange(1111111111,9999999999)

    accnumber = gen('self')

    def deposit2_database(connection, query):
        con = sqlite3.connect('product.db')
        cursor = con.cursor()
        try:
            cursor.execute(f"UPDATE bank SET account_balance = '12 years' ")
        except KeyError:
            print("Error")

    def deposit2(self):
        try:
            con = sqlite3.connect('product.db')
            cursor = con.cursor()
            h = int(input('Which account do you want to deposit cash into\n1.Savings account\n2.Current account\n'))
            if h == 1:
                amount = int(input('Enter how much you want to deposit into your savings account\n'))
                account_bal = self.savings_account.append(amount)
                print('\nPlease wait while we process your request\n')
                time.sleep(2.0)
                try:
                    cursor.execute(f"UPDATE bank SET account_balance = '{account_bal}' ")
                    print(f'You have successfully deposited N{amount} into your savings account and your account balance is N{account_bal}')
                except KeyError:
                    print("Error")
            elif h == 2:
                amount = int(input('Enter how much you want to deposit into your current account\n'))
                acct_bal = self.current_account.append(amount)
                print('\nPlease wait while we process your request\n')
                time.sleep(2.0)
                print(f'You have successfully deposited N{amount} into your current account and your account balance is N{acct_bal}')
            else:
                print('Invalid selection number,Please retry')
                try:
                    p = int(input('Would you like to\n1.Exit?\n2.Or go back to the previous page\n'))
                    if p == 1:
                        exit()
                    elif p == 2:
                        self.deposit()
                    else:
                        print('Invalid selection number')
                except ValueError:
                    print('Error!, only numbers(integers) needed')
        except ValueError:
            print('Error!, only numbers(integers) needed')
        con.commit()
        con.close()



    def deposit(self):
        con = sqlite3.connect('product.db')
        cursor = con.cursor()
        fullname = input('Enter your fullname\n')
        user_account_number =int(input('Enter your account number\n'))
        pin = int(input('Enter your 4 digit pin number\n'))
        for user_account_number,p in self.customers.items():
            if user_account_number == self.accnumber:
                if p[2] == pin:
                    cursor.execute((self.deposit2()))
                    break
        else:
            print('Sorry! you have entered an invalid name or account number\nCreate a new account?\n')
            try:
                r = int(input('Do you want to continue?\n1.Yes\n2.No\n'))
                if r == 1:
                    self.createacc()
                elif r == 2:
                    try:
                        p = int(input('Would you like to\n1.Exit?\n2.Or go back to the previous page\n'))
                        if p == 1:
                            exit()
                        elif p == 2:
                            self.deposit()
                        else:
                            print('Invalid selection number')
                    except ValueError:
                        print('Error!, only numbers(integers) needed')
                else:
                    print('Invalid selection number,Please retry')
            except ValueError:
                print('Error!, only numbers(integers) needed')
        con.commit()
        con.close()


    def withdraw2(self):
        try:
            w = int(input('Which account do you want to withdraw cash from\n1.Savings account\n2.Current account\n'))
            if w == 1:
                amount = int(input('Enter the amount you want to withdraw\n'))
                account_balance = (self.savings_account - amount)
                if self.savings_account > amount:
                    print('Please wait, while we process your request')
                    time.sleep(2.0)
                    print(f'You have successfully withdrawn N{amount} from your account and your account balance is N{account_balance}')
                else:
                    print('Insufficient balance')
            elif w == 2:
                amount = int(input('Enter the amount you want to withdraw'))
                acct_balance = (amount - self.current_account)
                if self.current_account > amount:
                    print('Please wait, while we process your request')
                    time.sleep(2.0)
                    print(f'You have successfully withdrawn N{amount} from your account and your account balance is N{acct_balance}')
                else:
                    print('Insufficient balance')
            else:
                print('Invalid selection number,Please retry\n')
                try:
                    p = int(input('Would you like to\n1.Exit?\n2.Or go back to the previous page\n'))
                    if p == 1:
                        exit()
                    elif p == 2:
                        self.withdraw()
                    else:
                        print('Invalid selection number')
                except ValueError:
                    print('Error!, only numbers(integers) needed')
        except ValueError:
            print('Error!, only numbers(integers) needed')

    def withdraw(self):
        fullname = input('Enter your fullname\n')
        user_account_number = int(input('Enter your account number\n'))
        pin = int(input('Enter your pin number\n'))
        for user_account_number,p in self.customers.items():
            if user_account_number == self.accnumber:
                if p[2] == pin:
                    self.withdraw2()
                    break
        else:
            print('Create new account\n')
            try:
                r = int(input('Do you want to continue?\n1.Yes\n2.No\n'))
                if r == 1:
                    self.createacc()
                elif r == 2:
                    try:
                        p = int(input('Would you like to\n1.Exit?\n2.Or go back to the previous page\n'))
                        if p == 1:
                            exit()
                        elif p == 2:
                            self.withdraw()
                        else:
                            print('Invalid selection number')
                    except ValueError:
                        print('Error!, only numbers(integers) needed')
                else:
                    print('Invalid selection number,Please retry')
            except ValueError:
                print('Error!, only numbers(integers) needed')

    def createacc(self):
        con = sqlite3.connect('product.db')
        cursor = con.cursor()
        try:
            cursor.execute("""CREATE TABLE bank (fullname TEXT char(30), 
                email TEXT char(50) , age INT n(2) , pin TEXT n(4) , tel_number TEXT n(11) , accnumber INT(10) ,
                account_type TEXT char(20) , account_balance INT n(9) )""")
        except sqlite3.OperationalError:
            fullname = input('\nEnter your full name\n')
            if len(fullname) > 1:
                pass
                email = input('\nEnter a valid email address\n')
                if '@gmail.com' in email:
                    pass
                    try:
                        age = input('\nEnter your age\n')
                        if len(age) <= 18:
                            pass
                            pin = int(input('\n**Make sure the 4 digit number you are gonna enter can be remembered to avoid complications while acessing your account**\nEnter a 4 digit number\n'))
                            try:
                                tel_number =input('\nEnter your mobile number\n')
                                if len(tel_number) == 11:
                                    pass
                                    self.gen()
                                    try:
                                        account_type = str(input('\nWhich type of account do you want to open\n*Savings account\n*Current account\n'))
                                        if account_type == 'Savings account':
                                            pass
                                            account_balance = (0.00)
                                            print('\nPlease wait, while we process your bank details\n')
                                            time.sleep(2.0)
                                            user_account_number = self.accnumber
                                            self.customers[user_account_number] = [fullname,email,pin,tel_number,account_type]
                                            final_output = (f'''Dear {fullname} you have successfully created a Savings bank account
                **Here are your account details**
                    *Account name: {fullname}
                    *Account number: {self.accnumber}
                    *User pin: {pin}
                    *Account type: {account_type}
                    *Account balance:N{tuple(self.savings_account)}''')
                                            print(final_output)
                                            print('Now login with your details\n')
                                            self.login()
                                        elif account_type == 'Current account':
                                            print('\nPlease wait, while we process your bank details\n')
                                            time.sleep(2.0)
                                            self.gen()
                                            user_account_number = self.accnumber
                                            self.customers[user_account_number] = [fullname,email,pin,tel_number,account_type]
                                            finaloutput = (f'''Dear {fullname} you have successfully created a Current bank account 
                **Here are your account details**
                    *Account name: {fullname}
                    *Account number: {self.accnumber}
                    *User pin: {pin}
                    *Account type: {account_type}
                    *Account balance:N{tuple(self.current_account)}''')
                                            print(finaloutput)
                                            print('Now login with your details\n')
                                            self.login()
                                        else:
                                            print('Invalid selection')
                                    except ValueError:
                                        print('Error!, enter the account_type you want to use.')
                                else:
                                    print('\nIncorrect mobile number')
                            except ValueError:
                                print('Error!, only numbers(integers) needed')
                        else:
                            print('You are not upto required age (you must be more than 18)')
                    except ValueError:
                        print('Error!, only numbers(integers) needed')
                else:
                    print('\nInvalid email address')
            else:
                print('\nInvalid name')
        cursor.execute(""" INSERT INTO bank (fullname,email,age,pin,tel_number,accnumber,account_type,account_balance) 
        VALUES (?,?,?,?,?,?,?,?)
        """,(fullname,email,age,pin,tel_number,self.accnumber,account_type,account_balance))
        con.commit()
        con.close()

    # def database():
    #     con = sqlite3.connect('product.db')
    #     cursor = con.cursor()
    #     get = cursor.execute("""SELECT * FROM bank WHERE rowid = 1 """)
    #     for g in get:
    #         print(list(g)[2])
    #     con.commit()
    #     con.close()

    def check(self):
        try:
            fullname = input('Enter your full name\n')
            user_account_number = int(input('Enter your account number\n'))
            pin = int(input('Enter your 4 digit pin number\n'))
            self.customers[self.accnumber]=[fullname,self.accnumber,pin]
            for user_account_number,p in self.customers.items():
                if user_account_number == self.accnumber:
                    if p[2] == pin:
                        j = int(input('1.Savings account\n2.Current account\n'))
                        if j == 1:
                            print('Please wait, while we process your request')
                            time.sleep(2.0)
                            print(f'Your Savings bank account balance = {self.savings_account}')
                        elif j == 2:
                            print('Please wait, while we process your request')
                            time.sleep(2.0)
                            print(f'Your Current bank account balance = {self.current_account}')
                        else:
                            print('Invalid selection number,Please retry')
                            break
                else:
                    print('Sorry! you have entered an invalid name or account number')  
        except ValueError:
            print('Error!, only numbers(integers) needed')
            self.check()
            # con.commit()
            # con.close()

    def exit(self):
        try:
            p = int(input('Are you sure you want to exit\n1.Yes\n2.No\n'))
            if p == 1:
                print('Thanks for banking with us')
            else:
                self.options()
        except ValueError:
            print('Error!, only numbers(integers) needed')
            exit()


    def login(self):
        self.options()

    def options(self):
        try:
            p = int(input('Do you want to\n1.Deposit cash?\n2.Withdraw cash?\n3.Check your account balance?\n4.Exit\n'))
            if p == 1:
                self.deposit()
            elif p == 2:
                self.withdraw()
            elif p == 3:
                self.check()
            elif p == 4:
                exit()
            else:
                print('Invalid selection number,Please retry')
                self.options()
        except ValueError:
            print('Error!, only numbers(integers) needed')
            self.options()

    def bank(self):
            print('\nWelcome to Microfinance Bank\n')
            try:
                choice = int(input('Do you have an account with us\n1.Yes\n2.No\n'))
                if choice == 1:
                    self.options()
                elif choice == 2:
                    self.createacc()
                else:
                    print('Invalid selection number,Please retry\n')
            except ValueError:
                print('Error!, only numbers(integers) needed')
                self.bank()
   
instance = Bank()

instance.gen()
instance.deposit2()
instance.deposit()
instance.withdraw2()
instance.withdraw()
instance.createacc()
instance.check()
instance.exit()
instance.login()
instance.options()
instance.bank()
