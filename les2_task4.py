"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

inString = input("Введите строку из слов разделенную пробелами: ")

#inString = "sdf sdf sdfq ereqwr eqwrqw qwr fg R AWR egrytyrdgfgretyerfg et ewATFSDFAWRewtgfzfdgerygzdds"

list_string = inString.split(" ")

for numb, item in enumerate (list_string):
    print (numb+1, " ", item[:10])

