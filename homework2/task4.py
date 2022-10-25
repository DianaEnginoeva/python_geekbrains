# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

number = int(input('Введите число N: ')) 
multiplied_numbers = input('Введите позиции элементов: ').split() 

def list_creator(number):
	# список от -N до N
	numbers_list = [x for x in range (-number, number+1)]
	print(numbers_multiplication(numbers_list, multiplied_numbers))

def numbers_multiplication(numbers_list, multiplied_numbers):
	result = 1
	for i in multiplied_numbers:
		if int(i) < len(numbers_list):
			result *= numbers_list[int(i)]
		else:
			return (f'Данного значения нет в списке: {int(i)}')
	return result

list_creator(number)

