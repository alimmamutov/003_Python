# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
# по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
#
# Как поступить, если потребуется сортировка по ключам?




def thesaurus_adv(*args):
    myDict = {}
    for elements in args:
        namesurname = elements.split()
        myDict.update({'name':namesurname[0]})
        myDict.update({'surname': namesurname[1]})
        myDict.update({'nameFirstSymbol': namesurname[0][0]})
        myDict.update({'surnameFirstSymbol': namesurname[1][0]})
        print(myDict)



    return myDict


def thesaurus(*args):
    myDict = {}
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


myAdvThesaurus = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# myThesaurus = thesaurus("Иван", "Мария", "Петр", "Илья", "Алим")
# print(myThesaurus)

