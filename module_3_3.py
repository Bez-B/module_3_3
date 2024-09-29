def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print()
print('1. Функция с параметрами по умолчанию')
print()

print_params()
print_params(0)
print_params(-1, 'string')
print_params(7, 'str', False)

print_params(b=25)  # Такой вызов работает, но функция ожидала тип данных str, а получила int
print_params(c=[1,2,3])  # Такой вызов работает, но функция ожидала тип данных bool, а получила list[int]

print()
print('2. Распаковка параметров')
print()

values_list = ['Urban', (3, 7, 15), True]
values_dict = {'a': 33, 'b': 'URBAN UNIVERSITY', 'c': False}

print_params(*values_list)
print_params(**values_dict)

print()
print('3. Распаковка + отдельные параметры')
print()

value_list_2 = [6 * 7, 'равно сорок два']

print_params(*value_list_2, 42)  # Работает

print()
print('Все работает, УРА!')