import sys
with open('bakery.csv', 'a', encoding='utf-8') as f:
    newLine = f'{round(float(sys.argv[1]),2)}\n'
    f.write(newLine)
