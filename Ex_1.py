# Lesson1
durations = {'min': 60, 'hour': 3600, 'day': 86400, 'month': 2678400, 'year': 977616000}

user_sec = int(input('Введите количество секунд: '))
sec_count = user_sec

years = sec_count // durations['year']
sec_count = sec_count - years*durations['year']

months = sec_count // durations['month']
sec_count = sec_count - months*durations['month']

days = sec_count // durations['day']
sec_count = sec_count - days*durations['day']

hours = sec_count // durations['hour']
sec_count = sec_count - hours*durations['hour']

minuts = sec_count // durations['min']
sec_count = sec_count - minuts * durations['min']

format_str = f'{user_sec} секунд = {years} лет ' \
             f'{months} месяцев ' \
             f'{days} дней ' \
             f'{hours} часов ' \
             f'{minuts} минут ' \
             f'{sec_count} секунд '
print(format_str)
