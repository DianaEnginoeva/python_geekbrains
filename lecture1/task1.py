# переменные, числа, строки, логический тип
print('hello world')

value = None
# определяем тип переменной
print(type(value))

a = 5
print(type(a))

b = 10.2
print(type(b))

value = 3821
print(type(value))

# СТРОКИ

name = 'Diana'
print(name)

# name = 'I'm Diana' - это выведет ошибку из-за кавычки
# но есть решение
name = "I'm Diana"
print(name)

# решений, конечно, несколько (это экранирование, если ты забыла)
name = 'I\'m Diana 2'
print(name)

# выводим несколько переменных сразу (интерполяция)
print(a, b, name)
print(a, ' - ', b, ' - ', name)
print('{}  -  {}  -  {}'.format(a, b, name))
print(f'{a}  -  {b}  -  {name}')

# меняем местами переменные
print('{2}  -  {0}  -  {1}'.format(a, b, name))
# выведет I'm Diana 2  -  5  -  10.2 вместо 5  -  10.2  -  I'm Diana 2


# ЛОГИЧЕСКИЕ ПЕРЕМЕННЫЕ
f = True
print(f)

f = False
print(f)

# СПИСКИ
list = []
print(list)

list = [1,2,3]
print(list)

list = ['1',2,3]
print(list)