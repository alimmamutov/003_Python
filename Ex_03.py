import itertools

keys = ['User', 'Hobbies']
newDict = []
with open('ex_3_users.csv', 'r', encoding='utf-8') as f1, open('ex_3_hobbies.csv', 'r', encoding='utf-8') as f2:
    content1 = f1.read().strip().splitlines()
    content2 = f2.read().strip().splitlines()
    if len(content1) >= len(content2):
        myList = list(itertools.zip_longest(content1, content2))
        for element in myList:
            newDict.append(dict(zip(keys, element)))
    else:
        print(1)
    print(newDict)