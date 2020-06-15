"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[

(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})

]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{

“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]

}
"""

goods = []
list_goods = []
dict_goods = {}
list_tuple = []

# тестовый набор данных

# dict_goods["название"] = "qwer"
# dict_goods["цена"] = 2
# dict_goods["количество"] = 3
# dict_goods["ед"] = "po"
# list_goods.append(1)
# list_goods.append(dict_goods.copy())
# list_tuple.append(tuple(list_goods))
# dict_goods.clear()
# list_goods.clear()
# dict_goods["название"] = "asdf"
# dict_goods["цена"] = 4
# dict_goods["количество"] = 5
# dict_goods["ед"] = "po"
# list_goods.append(2)
# list_goods.append(dict_goods.copy())
# list_tuple.append(tuple(list_goods))
# dict_goods.clear()
# list_goods.clear()

NumbsGoods = int (input ("Введите количество товаров: "))
for number in range (NumbsGoods):
    print ("Введите информацию о товаре", number+1)
    NameGods = input ("Введите название товара: ")
    dict_goods["название"] = NameGods
    NameGods = int(input ("Введите цену товара: "))
    dict_goods["цена"] = NameGods
    NameGods = int(input ("Введите количество товара: "))
    dict_goods["количество"] = NameGods
    NameGods = input ("Введите единицу измерения: ")
    dict_goods["ед"] = NameGods
    list_goods.append(number+1)
    list_goods.append(dict_goods.copy())
    list_tuple.append(tuple(list_goods))
    dict_goods.clear()
    list_goods.clear()



print ("Введенные данные: ", list_tuple)

analitic_goods = {}

numb = 0

for number, item in list_tuple:
    for item_key in item.keys():
        if numb == 0:
            analitic_goods[item_key] = []
        analitic_goods[item_key].append(item.get(item_key))

    numb += 1

# Единица измерения товара должна быть указана для каждого товара, иначе при разных данных об единицах измерения
# товара могут быть пропуски и будет непонятно где какая единица измерения.
print ("Аналитика о товарах:")
print (analitic_goods)




