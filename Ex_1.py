#Lesson1 епаоенпол6ерен
durations = {'min': 60,'hour': 3600,'day': 86400,'month': 2678400,'year': 977616000}

user_sec = int(input('Введите количество секунд: '))
sec_count = user_sec

years = sec_count // durations['year']
sec_count = sec_count - years*durations['year']
print(years)
print(sec_count)

months = sec_count // durations['month']
sec_count = sec_count - years*durations['month']
print(sec_count)

days = sec_count // durations['day']
sec_count = sec_count - months*durations['day']
print(sec_count)

format_str = f'{years} лет {months} месяцев {days} дней'
print(format_str)
