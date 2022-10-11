# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

# line = [1,2,2,3,3]
line = input("Введите строку: ")

list_line = []
list_line.append(line[0])

for i in range(len(line)-1):
    
    if line[i] != line[i+1]:
        list_line.append(line[i+1])
    else: continue

print(list_line)