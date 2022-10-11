# ПОДРОБНЕЕ О СТРОКАХ

text = 'Квоффлик любит чаппи'

# кол-во символов
print(len(text)) #20

# проверить наличие подстроки
print('чаппи' in text) #true

# являются ли все символы строки числами
print(text.isdigit()) #false

# являются ли все символы строки символами нижнего регистра
print(text.islower()) #false

# сделать замену
print(text.replace('чаппи', 'китикэт')) #Квоффлик любит китикэт

# СРЕЗЫ
# вывести первый символ
print(text[0]) #К

# вывести последний символ (-1, тк индексация с нуля)
print(text[len(text)-1]) #и

# вывести 5 с конца символ
print(text[-5]) #ч

# вывести от 0 до len(text)-1 (от первого до последнего символа)
print(text[:])

# вывести от 0 до 2
print(text[:2]) #Кв

# вывести от 1 до -2 (до 3 с конца включительно)
print(text[1:-2]) #воффлик любит чап