import re


def email_parse(email_address):
    result = re.fullmatch(r'(?P<Username>[A-Za-z!._-]+)@(?P<Domain>[A-Za-z]+\.\w{2,})', email_address)
    if result is None:
        raise ValueError(f'Невалидный email {email_address}')
    return result.groupdict()


if __name__ == '__main__':
    email_list = ["someone@geekbrains.ru", 'someone@geekbrainsru',
                  'mamutov.creation@yandex.ru', 'mamutov-alim@geekbrains.ru']
    for email in email_list:
        try:
            print(email_parse(email))
        except ValueError as e:
            print(e.args)
