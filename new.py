# a=('amarachi')
# print(type(a))
# x=(17)
# print(type(x))
# d=(19.0)
# print(type(d))
# h=('blue')
# print(type(h))

# a recursive function
# def add(number):
#     if number:
#         return add + number(number-1)
#     else:
#         return 0 

# new = add(10)
# print(new)


#3. write a python program to sort a list of tuples using lambda
# original list of tuples:
# [('english',88),('science',90),('maths',97),('social ssciences',82)]
# sorting the list of tuples:
#[('social ssciences',82),('maths',97),('science',90),('english',88)]


# subjects = [('english',88),('science',90),('maths',97),('social sciences',82)]
# total = lambda x:(x),subjects
# re = reversed(total)
# for x in re:
#     print(x)


# vary = 5
# another = int(input('how long'))
# while another > 5:
#     vary *= another
#     another = int(input('how long'))
#     print(vary)

# write a python program to convert month name to a number of days
# expected output:list of months(january,february,march,april,may),
# input name of month:february,
# no 0f days:28/29 days.
# days = 31,'days'
# day = 28,'days'
# dayss = 30,'days'
# months = ('1.january\n2.february\n3.march\n4.april\n5.may\n')
# print(months)


# month = int(input('name of month\n'))
# if month == 1 or 3 or 5:
#     days == month
#     print(days)
# elif month == 2:
#     day == month
#     print(day)
# while month == 4:
#     dayss == month
#     print(dayss)

months = ['','1. january','2. february''3. march','4. april','5. may','6. june','7. july','8. august','9. september','10. october','11. november','12. december']
choose = int(input('input name of month\n'))
days = 30
day = 31
time = 28/29
if choose == months.index('4. april'):
    print(f'april have {days} days in its month')
elif choose == months.index('6. june'):
    print(f'june have {days} days in its month')
elif choose == months.index('9. september'):   
    print(f'september have {days} days in its month')
elif choose == months.index('11. november'):
    print(f'november have {days} days in its month')
elif choose == months.index('1. january'):
    print(f'january have {day} days in its month')
# elif choose == months.index('3. march'):
#     print(f'march have {day} days in its month')
elif choose == months.index('5. may'):
    print(f'may have {day} days in its month')
elif choose == months.index('7. july'):
    print(f'july have {day} days in its month')
elif choose == months.index('8. august'):
    print(f'august have {day} days in its month')
elif choose == months.index('10. october'):
    print(f'october have {day} days in its month')
elif choose == months.index('12. december'):
    print(f'december have {day} days in its month')
elif choose == months.index('2. february'):
    print(f'february have {time} days in its month')
else:
    print('invalid')
















