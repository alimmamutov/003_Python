newList = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        element = line.replace('"', '').split(' ')
        newList.append(element[0])

ipSetList = list(set(newList))
countIpList = []
for element in ipSetList:
    countIpList.append(newList.count(element))
genList = list(zip(ipSetList,countIpList))
genList.sort(key = lambda x: x[1], reverse=True)
print(f"Спаммр - {genList[0][0]}")
