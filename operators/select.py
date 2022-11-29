a=input('enter the first value')
b=input('enter the second value')
print(f'{a},{b}')
if (a>b or b>a):
    print('its true')
elif (a<b and a>b):
    print('a is less than b and a is greater than b')
elif (a>b or b!=a):
    print('a is greater than b or b is not equal to a')
elif not(b==a or b<a):
    print('b equal to a or b less than a')
elif (b<a and a>b):
    print('b is less than a and a is greater than b')
elif (a==b and b==a):
    print('a is equal to b and b is equal to a')
else:
    print('nothing happened')






