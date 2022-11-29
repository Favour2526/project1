class Phones:
    
    products = []
    
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
        Phones.products.append(self)
    def display(self):
        print(f'\nProduct name = {self.name}\nProduct quantity = {self.quantity}\nProduct price = {self.price}')
    def __repr__(self):
        return f'\nProduct name = {self.name}\nProduct quantity = {self.quantity}\nProduct price = {self.price}\nThe totalprice of the product = {self.quantity * self.price}'
    

tecnophone = 70000
infinixphone = 95000
choice = int(input('''Choose the brand of phone you want to buy\n
    1.Tecno phones
    2.Infinix phones
'''))
if choice == 1:
    Tphones = int(input('''Which model of tecno phones do you want to buy\n
    1.Tecno Pop5
    2.Tecno Spark6
    3.Tecno Camon15\n'''))
    quantity = int(input('Enter the quantity of product you want to buy\n'))
    if Tphones == 1:
        item1 = Phones('Tecno Pop5',quantity,tecnophone)
        print(item1.display)
    elif Tphones == 2:
        item12 = Phones('Tecno Spark6',quantity,tecnophone)
        print(item12.display)
    elif Tphones == 3:
        item13 = Phones('Tecno Camon15',quantity,tecnophone)
        print(item13.display)
    else:
        print('Invalid selection number')
elif choice == 2:
    Ixphones = int(input('''Which model of infinix phones do you want to buy\n
    1.Infinix Hot8
    2.Infinix Smart6
    3.Infinix Hot10\n'''))
    quantity = int(input('Enter the quantity of product you want to buy\n'))
    if Ixphones == 1:
        item2 = Phones('Infinix Hot8',quantity,infinixphone)
        print(item2.display)
    elif Ixphones == 2:
        item21 = Phones('Infinix Smart6',quantity,infinixphone)
        print(item21.display)
    elif Ixphones == 3:
        item22 = Phones('Infinix Hot10',quantity,infinixphone)
        print(item22.display)
    else:
        print('Invalid selection number')     
else:
    print('Invalid selection number')




