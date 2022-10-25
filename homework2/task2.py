# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# Пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите число: "))

def numbers_multiplication(number):
	count = 1

	for i in range(number):
		i = i + 1
		count = i * count
		
		print(count)

numbers_multiplication(number)