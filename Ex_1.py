# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.

# initialize dictionary
NUMBERS_DICT = {'ONE': 'Один',
                'TWO': 'Два',
                'THREE': 'Три',
                'FOUR': 'Четыре',
                'FIVE': 'Пять',
                'SIX': "Шесть",
                'SEVEN': "Семь",
                'EIGHT': "Восемь",
                'NINE': "Девять",
                'TEN': "Десять"
                }


def num_translate(english_word):
    return NUMBERS_DICT.get(english_word.upper(),"Перевод не задан")


userNumber = input('Number in english: ')
print(num_translate(userNumber))

