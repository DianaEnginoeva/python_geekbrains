# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого
# Например:
# 5, 25 -> да
# 25, 5 -> да
# 8, 9 -> нет

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

def checking(num1, num2):
	checker1 = num1 == num2**2
	checker2 = num2 == num1**2

	if checker1 == True or checker2 == True:
		result = 'да'
	else:
		result = 'нет'

	return result

print(checking(num1, num2))