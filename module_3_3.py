def print_params( a=1, b='строка', c=True):
    print(a, b, c)


# Вызов функции

print_params()
print_params(10)
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров

values_list= [5, 'hello', False]
values_dict= {'a': 100, 'b': 'world' , 'c': True }

print_params(*values_list)
print_params(**values_dict)


# Распаковка + отдельные параметры

values_list_2= [ 38.31, 'Строка']

print_params(*values_list_2, 42)