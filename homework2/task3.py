# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

number = int(input('Введите число: ')) 

def sequence(number):
	return[round((1 + 1 / x)**x, 2) for x in range (1, number + 1)]
print(sequence(number))
print(round(sum(sequence(number)), 2))