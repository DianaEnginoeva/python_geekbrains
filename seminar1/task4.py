# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа
number = float(input("Введите число: "))

def float_first(number):
	if number>0:
		result = int(number * 10 % 10)
	elif number<0:
		result = int(number * -10 % 10)
	else:
		result = "дробной части нет"
	
	return result

print(float_first(number))