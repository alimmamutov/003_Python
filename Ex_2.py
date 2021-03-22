# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с
# числительными, начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

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


def num_translate_adv(english_word):
    translation = NUMBERS_DICT.get(english_word.upper(), "Перевод не задан")
    first_symbol = translation[0]
    if english_word[0].isupper():
        first_symbol = translation[0].upper()
    else:
        first_symbol = translation[0].lower()
    return f'{first_symbol}{translation[1:]}'


userNumber = input('Number in english: ')
print(num_translate_adv(userNumber))
