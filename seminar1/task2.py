# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

numbers = []

num1 = int(input("Введите первое число: "))
numbers.append(num1)
num2 = int(input("Введите второе число: "))
numbers.append(num2)
num3 = int(input("Введите третье число: "))
numbers.append(num3)
num4 = int(input("Введите четвертое число: "))
numbers.append(num4)
num5 = int(input("Введите пятое число: "))
numbers.append(num5)

print(max(numbers))