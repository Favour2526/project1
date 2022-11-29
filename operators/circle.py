#formula for the area of a circle= ^r2(pie Rsquared)
# x or ^(pie)=22/7 or 3.14
# r=21
# 2=squared
# x=22/7

# # create a function with variable length of argument
# def data(*numbers):
#     for a in numbers:
#         print(a)

# data(20,40,60)

# def words(*meaning):
#     meaning = key
# key ={'man':'a male living organism',
#         'woman':'a female living organism',
#     'child':'a  little being'
# }
# for k, v in key.items():
#     print(key)
# words(k,v)



#2. write a python program to create a function that takes one argument and
# that argument will be multiplied with an unknown given number.
# sample output:
# double the number of 15 =30
# triple the num of 15 = 45
# quadruple the num of 15 = 60
# Quintuple the num of 15 = 75


product = lambda x:(x)
y = 15
print(f'double the number of 15 = {product(2,15)}')
print(f'triple the number of 15 = {product(3,15)}')
print(f'quadruple the number of 15 = {product(4,15)}')
print(f'quintuple the number of 15 = {product(5,15)}')