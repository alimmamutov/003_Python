import sys
#
with open('bakery.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    if len(sys.argv) == 1:
        for line in lines[1:]:
            print(line.strip())
    elif len(sys.argv) == 2:
        for line in lines[int(sys.argv[1]):]:
            print(line.strip())
    elif len(sys.argv) == 3:
        for line in lines[int(sys.argv[1]):int(sys.argv[2])+1]:
            print(line.strip())
    else:
        print('Error')