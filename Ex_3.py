#   Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем
#   «5 процентов», задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.

for i in range(1, 21):
    if i > 4:
        print(f"{i} процентов")
    elif i > 1:
        print(f"{i} процента")
    else:
        print(f"{i} процент")