# Create a function taking a positive integer as its parameter and returning a string
# containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the
# left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered:
# 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII;
# 1666 uses each Roman symbol in descending order: MDCLXVI.

# Example:

# solution(1000) # should return 'M'
# Help:

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

# Remember that there can't be more than 3 identical symbols in a row.

# 2543 -> MMDXLIII

num = int(input('Введите число: '))
result = ''

while num >= 1:
	if num >= 1000:
		count_m = num // 1000
		for i in range(count_m):
			rom = 'M'
			result = result + rom
			num %= 1000
	if num >= 900:
		count_cm = num // 900
		for i in range(count_cm):
			rom = 'CM'
			result = result + rom
		num %= 900
	if num >= 500:
		count_d = num // 500
		for i in range(count_d):
			rom = 'D'
			result = result + rom
		num %= 500
	if num >= 400:
		count_cd = num // 400
		for i in range(count_cd):
			rom = 'CD'
			result = result + rom
		num %= 400
	if num >= 100:
		count_c = num // 100
		for i in range(count_c):
				rom = 'C'
				result = result + rom
		num %= 100
	if num >= 90:
		count_xc = num // 90
		for i in range(count_xc):
			rom = 'XC'
			result = result + rom
		num %= 90
	if num >= 50:
		count_l = num // 50
		for i in range(count_l):
				rom = 'L'
				result = result + rom
		num %= 50
	if num >= 40:
		count_xl = num // 40
		for i in range(count_xl):
			rom = 'XL'
			result = result + rom
		num %= 40
	if num >= 10:
		count_x = num // 10
		for i in range(count_x):
				rom = 'X'
				result = result + rom
		num %= 10
	if num >= 9:
		count_ix = num // 9
		for i in range(count_ix):
			rom = 'IX'
			result = result + rom
		num %= 9 
	if num >= 5:
			count_v = num // 5
			for i in range(count_v):
					rom = 'V'
					result = result + rom
			num %= 5
	if num >= 4:
		count_iv = num // 4
		for i in range(count_iv):
			rom = 'IV'
			result = result + rom
		num %= 4
	if num >= 1:
			count_i = num // 1
			for i in range(count_i):
					rom = 'I'
					result = result + rom
			num %= 1

print(result)


