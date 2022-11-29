try:
    a =int(input('enter a number'))
    b = 10 / a
    print(b)
except ValueError:
    print('please only numbers needed')
except ZeroDivisionError:
    print(f'cant divide 10 by {a}')
    while a < 1:
        try:
            a =int(input('enter a number'))
            b = 10 / a
            print(b)
        except ZeroDivisionError:
            print(f'cant divide 10 by {a}')
        except NameError:
            pass

            
