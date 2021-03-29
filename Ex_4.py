# # *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# # «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
# # по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# # >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# # {
# #     "А": {
# #         "П": ["Петр Алексеев"]
# #     },
# #     "С": {
# #         "И": ["Иван Сергеев", "Инна Серова"],
# #         "А": ["Анна Савельева"]
# #     }
# # }
# #
# # Как поступить, если потребуется сортировка по ключам?
#
#
# def thesaurus_adv(*args):
#     myList = []
#     myDict = {}
#     for elements in args:
#         nameSurname = elements.split()
#         currentItem = {}
#         currentItem.update({'name':nameSurname[0]})
#         currentItem.update({'surname': nameSurname[1]})
#         currentItem.update({'nameFirstSymbol': nameSurname[0][0]})
#         currentItem.update({'surnameFirstSymbol': nameSurname[1][0]})
#         myList.append(currentItem)
#         currentDict = myDict.get(currentItem['surnameFirstSymbol'])
#         if currentDict is None:
#             new_dict = thesaurus(currentItem)
#
#         myDict.update({currentItem['surnameFirstSymbol']: new_dict})
#
#     print(myList)
#     filterList = filter(lambda el: el['nameFirstSymbol'] == 'И', myList)
#     print(list(filterList))
#     print(myDict)
#     return currentItem
#
#
# def thesaurus(*args):
#     myDict = {}
#     for el in args:
#         current_key = el['nameFirstSymbol']
#         current_item = myDict.get(current_key)
#         if current_item is None:
#             new_list = [el]
#         else:
#             current_item.append(el)
#             new_list = current_item
#         myDict.update({current_key: new_list})
#     return myDict
#
#
# myAdvThesaurus = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

