newList = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        element = line.replace('"', '').split(' ')
        new_tuple = ({element[0]}, {element[5]}, {element[6]})
        newList.append(new_tuple)