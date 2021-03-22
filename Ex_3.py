# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?

myDict = {}


def thesaurus(*args):
    for el in args:
        current_key = el[0]
        current_item = myDict.get(current_key)
        if current_item is None:
            new_list = [el]
        else:
            current_item.append(el)
            new_list = current_item
        myDict.update({current_key: new_list})
    return myDict


myThesaurus = thesaurus("Иван", "Мария", "Петр", "Илья", "Алим")
print(myThesaurus)
print(dict(sorted(myThesaurus.items(), key=lambda t: t[0])))
