# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input("Введите число: ")

def numbers_sum(number):
	if float(number) < 0:
		number = float(number) * (-1)
	count = 0
	for i in str(number):
		if i != '.':
			count += int(i)
	return count

print(f'Сумма чисел равна {numbers_sum(number)}')