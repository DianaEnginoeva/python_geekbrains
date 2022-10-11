# ЛОГИЧЕСКИЕ ОПЕРАЦИИ

a = 1<4
print(a)

a = 1>4
print(a)

a = 1<4 and 5>4
print(a)

a = 1 == 4
print(a)

# неравенство
a = 1 != 4
print(a)

a = 'abc' == 'abc'
print(a) # true

b = [1,2,3]
c = [1,2,3]
a = b == c
print(a) # true

a = 1<2<5
print(a) # true

a = 1<0 or 5>4
print(a) #true

a = 1<0 or 5<4
print(a) #false

f=[1,2,3,4]
print(f)
print(not 2 in f) #false, тк 2 есть в f

is_odd = f[0] % 2 == 0
print(is_odd) #false, тк 1 - нечетное число

# то же самое
is_odd = not f[0] % 2
print(is_odd) #false, тк 1 - нечетное число

