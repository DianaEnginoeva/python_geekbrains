# Реализуйте алгоритм перемешивания списка.

numbers_list = input('Введите список: ').split()

def list_shuffle(numbers_list):
	current_list = numbers_list[:]
	for i in range(len(current_list)):
		index = int(len(numbers_list)/2)
		temp = current_list[i]
		current_list[i] = current_list[index]
		current_list[index] = temp
		numbers_list.pop()
	return current_list

print(numbers_list)
print(list_shuffle(numbers_list))