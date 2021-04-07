import sys
#
with open('bakery.csv', 'a', encoding='utf-8') as f:
    newLine = f'\n{round(float(sys.argv[1]),2)}'
    f.write(newLine)
