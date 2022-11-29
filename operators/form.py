firstname=input ('enter your first name\n')
lastname=input('enter your last name\n')
age=int (input('enter your age\n'))
#level=int (input('enter the level you are in'))
if age>10 and age<12:
    print(f'dear {firstname} {lastname} welcome to jss1')
elif age<14 and age>12:
    print(f'dear {firstname} {lastname} welcome to jss2')
elif age==14 and age<15:
    print(f'dear {firstname} {lastname} welcome to jss3')
elif age==18 and age<17:
    print(f'dear {firstname} {lastname} welcome to ss1')
else:
    print('your age is not in school')                
              


