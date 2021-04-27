import re

    #
    # @classmethod
    # def date_parse(cls, date_string):
    #     result = re.fullmatch(r'(?P<date>^\d\d)-(?P<month>\d\d)-(?P<year>\d\d\d\d)', date_string)
    #     if result is None:
    #         raise ValueError(f'Не валидная дата {date_string}')
    #     date_dict = result.groupdict()
    #     for key in date_dict.keys():
    #         date_dict[key] = int(date_dict[key])
    #     return date_dict


class Date:

    def __init__(self, date):
        self.date = date

    def __str__(self) -> str:
        return str(self.date)

    @classmethod
    def date_to_int(cls, param):
        date_lst = str(param).split('-')
        if len(date_lst) == 3:
            return map(int, date_lst)
        else:
            return 'invalid date'

    @staticmethod
    def valid(day: int, month: int, year: int):
        if day not in range(1, 31):
            return 'invalid day'
        elif month not in range(1, 12):
            return 'invalid month'
        elif year not in range(0, 9999):
            return 'invalid year'
        else:
            return 'All good'


# test
a = Date('15-10-2021')
print(Date.valid(*Date.date_to_int(a)))
