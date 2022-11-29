reputation=('what someone is known for')
cubersome=('very difficult to handle')
naive=('lacking experience')
python=('python is a high level programming language used to create websites.')
intellectual=('having the power of understanding for higher forms of knowledge or thoughts')

di = {
    'rep':reputation,
    'cu':cubersome,
    'na':naive,
    'py':python,
    'in':intellectual
}
searchword = input('search for a word: ')

if searchword == 'reputation':
    print(f"{searchword} means {di.get('rep')}")
elif searchword=='cubersome':
    print(f"{searchword} means {di.get('cu')}")
elif searchword=='naive':
    print(f"{searchword} means {di.get('na')}") 
elif searchword=='python':
    print(f"{searchword} means {di.get('py')}")
elif searchword=='intellectual':
    print(f"{searchword} means {di.get('rep')}")
else:
    print('nothing happened')    


