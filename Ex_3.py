# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

myLst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

myStr = ''
print(myStr)

for i, element in enumerate(myLst):

    currentDigit = ''
    currentDirection = ''
    newWord = element
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
            newWord = f'"{currentDirection}0{currentDigit}"'
        else:
            newWord = f'"{currentDirection}{currentDigit}"'
    myStr = f'{myStr} {newWord}'  # Можно было бы формировать строку с помощью ' '.join(myLst) за циклом

print(myLst)
print(myStr)
