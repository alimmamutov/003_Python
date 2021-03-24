# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# * Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# * Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# * Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# * Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.

import random
myList = []
for i in range(20):
    price = round(random.random()*100, 2)
    strPrice = str(price)
    rub = strPrice[:strPrice.find(".")]
    cop = strPrice[strPrice.find(".")+1:]
    if len(cop) == 1:
        cop = '0' + cop
    rubCop = int(rub + cop)
    priceStr = f'{rub} рублей {cop} копеек'
    myList.append([price, strPrice, rub, cop, rubCop, priceStr])
print('Вот рэндомный список:')
print(myList)
print()
print('Вот отсортированный список:')
for el in sorted(myList, key=lambda element: element[4]):
    print(el[5])
print()
print('Вот доказательство, что список не изменился:')
print(myList)
print()
print('Вот обратная последовательность:')
for el in sorted(myList, key=lambda element: element[4], reverse=True):
    print(el[5])
print()
print('Вот 5 самых дорогих цен по возрастанию:')
newList = sorted(myList, key=lambda element: element[4], reverse=True)[:5]
for el in sorted(newList, key=lambda element: element[4]):
    print(el[5])
