with open('ex_3_users.csv', 'r', encoding='utf-8') as f1, \
        open('ex_3_hobbies.csv', 'r', encoding='utf-8') as f2, \
        open('users_hobby.txt', 'w', encoding='utf-8') as f3:
    for line1 in f1:
        line2 = f2.readline()
        line2 = line2.strip() if line2.strip() != '' else None
        newLine = f'{line1.strip()}: {line2}\n'
        print(newLine)
        f3.write(newLine)