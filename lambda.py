# mylist = [1,5,4,6,8,11,3,12]
# newlist = list(filter(lambda x:(x%2 != 0) , mylist))

# print(newlist)

# numbers= (1,2,3,4)
# result = map(lambda x: x + x,numbers)
# print(list(result))



# letters = set('my name is amarachi')
# x = ('a','e','i','o','u')
# word = list(filter(lambda x:(x) , letters))
# for i in word:
#     if i in x:
#         print(i)


# write a python program to create a lambda function that adds 15 to a 
#given number passed in as an argument,also create a lambda fuction that
#multiplies argument x and argumment y and print the result
#sample output:25,48

maths = lambda b:(b + 15)
print(maths(10))


product = lambda x,y:(x*y)
print(product(12,4))