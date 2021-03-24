# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

myLst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

myStr = ''
print(myStr)

for i, element in enumerate(myLst):
    currentDigit = ''
    currentDirection = ''
    if element[0] == '+':
        currentDirection = '+'
        currentDigit = element[1:]
    elif element[0] == '-':
        currentDirection = '-'
        currentDigit = element[1:]
    else:
        currentDigit = element[:]

    if currentDigit.isdigit():
        if len(currentDigit) == 1:
            myLst[i] = f'"{currentDirection}0{currentDigit}"'
        else:
            myLst[i] = f'"{currentDirection}{currentDigit}"'
    myStr = f'{myStr} {myLst[i]}'  # Можно было бы формировать строку с помощью ' '.join(myLst) за циклом

print(myLst)
print(myStr)
