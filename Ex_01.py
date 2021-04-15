import re
EMAIL_LIST = ['someone@geekbrains.ru', 'someone@geekbrainsru', 'mamutov.creation@yandex.ru',
              'mamutov-creation@yandex.ru']
RE_EMAIL = re.compile(r'(?P<Username>[A-Za-z!._-]+)@(?P<Domain>[A-Za-z]+\.\w{2,})')


def email_parse(email_address):
    if not RE_EMAIL.match(email_address):
        raise ValueError(f'wrong email:{email_address}')
    print(RE_EMAIL.match(email_address).groupdict())


for element in EMAIL_LIST:
    try:
        email_parse(element)
    except ValueError as err:
        print(err)
