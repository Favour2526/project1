# class Phone:

#     def __init__ (self,name:str,quantity:int,price:float):
    
#         self.name = name
#         self.quantity = quantity
#         self.price = price

#     def product(self):
#         print(f'product name = {self.name},product quantity = {self.quantity}, product price = {self.quantity * self.price}')

# item1 = Phone('tecno pop5',15,90000)
# item2 = Phone('infinix hot8 lite',12,75000)


# item1.product()
# item2.product()



# class Person():

#     def __init__(self,name,Id):
#         self.name = name
#         self.Id =Id

#     def display(self):
#         print(f'my name is {self.name} and my Id number is {self.Id}')

# class NewPerson(Person):

#     def __init__(self,name,Id,tel_number):
#         self.tel_number = tel_number
#         Person.__init__(self,name,Id)

#     def display(self):
#         print(f'my name is {self.name},my Id number is {self.Id} and my mobile number is {self.tel_number}')

# a = NewPerson('favour',24,90)

# a.display()
# use the repr magic method and the dict magic method
#  use try and except

class Choice():
    def __init__(self,choice):
        self.choice = choice
    def display(self):
        if self.choice == 1:
            class Tecnoproducts():
                def __init__(self,products):
                    self.products = products
                def display(self):
                    if self.products == 1:
                        class TecnoPhone():
                            def __init__(self,name,quantity,price):
                                self.name = name
                                self.quantity = quantity
                                self.price = price
                            def display(self):
                                print(f'Product name = {self.name}\nProduct quantity = {self.quantity}\nProduct price = {self.price}')
                                print(f'The totalprice of the product = {self.price * self.quantity}\n')
                        quantity = int(input('Enter the number of product(s) you want to buy\n'))
                        tecnoprice = 70000  
                        item1 = TecnoPhone('Tecno Pop5',quantity,tecnoprice)
                        item1.display()
                    elif self.products == 2:
                        class Tecphone():
                            def __init__(self,name,quantity,price):
                                self.name = name
                                self.quantity = quantity
                                self.price = price
                            def display(self):
                                print(f'\nProduct name = {self.name}\nProduct quantity = {self.quantity}\nProduct price = {self.price}')
                                print(f'The totalprice of the product = {self.price * self.quantity}\n')
                        quantity = int(input('Enter the number of product(s) you want to buy\n'))
                        tecnoprice = 70000 
                        item2 = Tecphone('Tecno Spark5',quantity,tecnoprice)
                        item2.display()
                    elif self.products == 3:
                        class Tphone():
                            def __init__(self,name,quantity,price):
                                self.name = name
                                self.quantity = quantity
                                self.price = price
                            def display(self):
                                print(f'\nProduct name = {self.name}\nProduct quantity = {self.quantity}\nProduct price = {self.price}')
                                print(f'The totalprice of the product = {self.price * self.quantity}\n')
                        quantity = int(input('Enter the number of product(s) you want to buy\n'))
                        tecnoprice = 70000 
                        item3 = Tphone('Tecno Camon16',quantity,tecnoprice)
                        item3.display()
                    else:
                        print('Invalid selection number')
            b = int(input('Tecno products\n1.Tecno Pop5\n2.Tecno Spark5\n3.Tecno Camon16\n'))
            item8 = Tecnoproducts(b)
            item8.display()
        elif self.choice == 2:
            class InfinixProducts():
                def __init__(self,products):
                    self.products = products
                def display(self):
                    if self.products == 1:       
                        class InfinixPhones():
                            def __init__(self,name,quantity,price):
                                self.name = name
                                self.quantity = quantity
                                self.price = price
                            def display(self):
                                print(f'Product name = {self.name}\nProduct quantity = {self.quantity}\nProduct price = {self.price}')
                                print(f'The totalprice of the product = {self.price * self.quantity}\n')
                        quantity = int(input('Enter the number of product(s) you want to buy\n'))
                        infinixprice = 95000
                        item4 = InfinixPhones('Infinix Hot8 Lite',quantity,infinixprice)
                        item4.display()
                    elif self.products == 2:
                        class InfiniPhone():
                            def __init__(self,name,quantity,price):
                                self.name = name
                                self.quantity =quantity
                                self.price = price
                            def display(self):
                                print(f'\nProduct name = {self.name}\nProduct quantity = {self.quantity}\nProduct price = {self.price}')
                                print(f'The totalprice of the product = {self.price * self.quantity}\n')
                        quantity = int(input('Enter the number of product(s) you want to buy\n'))
                        infinixprice = 95000
                        item5 = InfiniPhone('Infinix Smart6',quantity,infinixprice)
                        item5.display()
                    elif self.products == 3:
                        class InfinixMobile():
                            def __init__(self,name,quantity,price):
                                self.name = name
                                self.quantity = quantity
                                self.price = price
                            def display(self):
                                print(f'\nProduct name = {self.name}\nProduct quantity = {self.quantity}\nProduct price = {self.price}')
                                print(f'The totalprice of the product = {self.price * self.quantity}\n')
                        quantity = int(input('Enter the number of product(s) you want to buy\n'))
                        infinixprice = 95000
                        item6 = InfinixMobile('Infinix Hot10',quantity,infinixprice)
                        item6.display()
                    else:
                        print('Invalid selection number')
            c = int(input('Infinix products-\n1.Infinix Hot8 Lite\n2.Infinix Smart6\n3.Infinix Hot10\n'))
            item7 = InfinixProducts (c)
            item7.display()
        else:
            print('Invalid selection number')
a = int(input('Choose the brand of phone you want to buy\n1.Tecno phones\n2.Infinix phones\n'))
items = Choice(a)
items.display()



