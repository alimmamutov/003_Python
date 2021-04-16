import re


compile_string = r'(?P<remote_addr>^[\w\d.:]+ )(?:- - \[)' \
                 r'(?P<request_datetime>(?:\d{,2}/[A-Z][a-z]{2}/\d{4}:(?:\d{2}:){2})(?:\d{2}) .{5})\] \"' \
                 r'(?P<request_type>[A-Z]{3,}) ' \
                 r'(?P<requested_resource>/(?:[a-zA-z0-9_/]{1,}))(?: .{1,}\d\" )' \
                 r'(?P<response_code>\d{3}) ' \
                 r'(?P<response_size>\d+)'

RE_PARSE = re.compile(compile_string)


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        match = RE_PARSE.findall(line)
        print(match)
        # if len(match) == 0:
        #     print(line)
