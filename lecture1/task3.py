# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ
# // - целочисленное деление
# % - остаток от деления
# ** - возведение в степень

a = 1.3
b = 3
c = a*b
print(c) # должно быть 3.9, но будет 3.9000000000000004 (из-за особенностей хранения данных в python)
# нужно округлить результат
c = round(a*b, 3) #после запятой - количество знаков
print(c)

# сокращенные операции
a = 0
a = a + 5
print(a)
#то же самое, что
a = 0
a += 5
print(a)