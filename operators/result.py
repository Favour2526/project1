score=int (input('enter your score'))
a=90
b=80
c=70
d=60
e=50
f=40
g=30
if score>a and score>c:
    print(f'{score} you placed the first position')
elif score<a and score>b:
    print(f'{score} you placed the second position')
elif score==c and score>c and score<b:
    print(f'{score} you placed the third position')
elif score<d and score>e:
    print(f'{score} you placed the fourth position')
elif score>e and score<f:
    print(f' {score} you placed the fifth position')
elif score>f and score<g:
    print(f'{score} you placed the last position')
else:
    print(f'{score} u didnt pass')




