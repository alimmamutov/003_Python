from requests import get, utils


def currency_rates(valutechar):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    # print(type(content))
    # print(content)
    content = content.replace('<ValCurs Date="02.04.2021" name="Foreign Currency Market">', '')
    content = content.replace('<?xml version="1.0" encoding="windows-1251"?>', '')
    content = content.replace('</ValCurs>','')
    myStr = content.split("</Valute>")
    for element in myStr[:]:
        print(element)

# charCode = input('Введите кодовое название валюты:')
currency_rates('EUR')
