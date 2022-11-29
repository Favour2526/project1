# def product(name,quantity,totalprice):
#     print(f'item bought= {name}\n quantity of product = {quantity}\n total = {totalprice}')
# print ('1.phone = 20000\n2.laptop = 60000\n 3.usb = 4500\n4.charger = 2000\n5.powerbank = 8000\n')
# gadgets=(input('enter the item you wanna buy\n'))
# quantity = int(input('enter the quantity of what you wanna buy\n'))
# if gadgets == '1' :
#     name = 'phone'
#     totalprice = 20000*(quantity)
# elif gadgets == '2':
#     name = 'laptop'
#     totalprice = 60000*(quantity)
# elif gadgets == '3':
#     name = 'usb'
#     totalprice = 4500*(quantity)
# elif gadgets == '4':
#     name = 'charger'
#     totalprice = 2000*(quantity)
# elif gadgets == '5':
#     name = 'powerbank'
#     totalprice = 8000*(quantity)
# else:
#     print('we dont have such item here')

# product(name,quantity,totalprice)


#4. write a python program to sort a list of dictionaries using lambda.
# go to the editor 
#original list of dictionaries:
#[{'make':'nokia','model':216,'color':'black'},{'make','mimax','mod
# el':2,'color':'gold'},{'make','samsung','model':7,'color':'blue'}]
# sorting the list of dictionaries:


dict = [{'make':'nokia','model':216,'color':'black'},
{'make':'mimax','model':2,'color':'gold'},
{'make':'samsung','model':7,'color':'blue'}]
original_list = sorted(dict)
print(original_list, key= lambda x: x(x))





