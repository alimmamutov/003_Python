import sys
import decimal
with open('bakery.csv', 'a', encoding='utf-8') as f:
    newLine = f'{str(decimal.Decimal(sys.argv[1]))}\n'
    f.write(newLine)
