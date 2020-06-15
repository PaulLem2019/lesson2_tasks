"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

# my_list = [45, 567, 6754, 564, 234, 234, 123, 23]
print ("Введите список. Окончание ввода - симовол '.' (точка)")
my_list = []
inString = ""
while (inString != '.'):
    inString = input()
    my_list.append(inString)

my_list.remove('.')

print ("Начальный список")
print (my_list)

for number in range(0, len(my_list)-1, 2):
    my_list[number], my_list[number+1] = my_list[number+1], my_list[number]

print ("Измененный список")
print (my_list)

