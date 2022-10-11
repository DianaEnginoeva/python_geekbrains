# СПИСКИ

numbers = [1,2,3,4,5]
print(numbers)

# создаем range от 1 до 5 включительно
ran = range(1,6)
# приводим range к списку и выводим
print(list(ran))

# обращение к элементу по индексу
print(numbers[2])
numbers[2] = 0
print(numbers[2])
print(numbers)

# длина списка
print('длина списка:', len(numbers))

# использование в цикле
for i in numbers:
	i*=2
	print(i)
print(numbers)

# добавление нового элемента в список
print(numbers)
numbers.append(44)
print(numbers)

numbers.append('15')
print(numbers)

# удаление элемента из списка
numbers.remove(44)
print(numbers)

# удаление элемента из списка 2
del numbers[1]
print(numbers)