from requests import get, utils
import sys

def parsing():
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    content = content.replace('<?xml version="1.0" encoding="windows-1251"?>', '')
    replaceable_statement = content[:content.find('>')+1]
    content = content.replace(replaceable_statement, '')
    content = content.replace('</ValCurs>', '')
    myStrList = content.split("</Valute>")
    myStrList.pop()
    new_list = []
    for element in myStrList:
        closing = element.find('>') + 1
        current_str = element[closing:]
        new_dict = {}
        while current_str != '':
            current_key = current_str[1:current_str.find('>')]
            current_str = current_str.replace(current_str[:current_str.find('>') + 1], '')
            current_value = current_str[:current_str.find(f'/{current_key}') - 1]
            current_str = current_str.replace(current_str[:current_str.find('>') + 1], '')
            new_dict.update({current_key: current_value})
        new_list.append(new_dict)
    return new_list


def currency_rates(valutechar=''):
    xml_list_dict = parsing()
    for element in xml_list_dict:
        if element['CharCode'].upper() == valutechar.upper():
            value = element['Value'].replace(',', '.')
            return float(value)
    return None


if __name__ == '__main__':
    program, *valList = sys.argv
    for val in valList:
        print(currency_rates(val))