# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def checking(x,y,z):
	result = not(x or y or z) == (not(x) and not(y) and not(z))
	return result

print(checking(0,0,0))
print(checking(0,0,1))
print(checking(0,1,0))
print(checking(0,1,1))
print(checking(1,0,0))
print(checking(1,0,1))
print(checking(1,1,0))
print(checking(1,1,1))