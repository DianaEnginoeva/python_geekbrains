# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
number = int(input("Введите число: "))

def numbers_output(number):
	i = -number
	while i<=number:
		print(i)
		i += 1

numbers_output(number)

# Еще один способ
# n = int(input("Введите число: "))

# for i in range(-n, n+1):
# 	print(i)

# В одну строку
# n = int(input("Введите число: "))

# for i in range(-n, n+1):
# 	print(i, end = " ")