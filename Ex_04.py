import os
import random


folder = 'some_data'


def generate_files():
    letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    for _ in range(10):
        f_name = ''.join(random.sample(letters, random.randint(5, 10)))
        f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(100)))
        with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
            f.write(f_content)

    for _ in range(10):
        f_name = ''.join(random.sample(letters, random.randint(5, 10)))
        f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10)))
        with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
            f.write(f_content)

    for _ in range(10):
        f_name = ''.join(random.sample(letters, random.randint(5, 10)))
        f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(1000)))
        with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
            f.write(f_content)
    for _ in range(10):
        f_name = ''.join(random.sample(letters, random.randint(5, 10)))
        f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10000)))
        with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
            f.write(f_content)


def show_size():
    myDict ={}
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_size = len(str(os.stat(os.path.join(root,file)).st_size))
            round_file_size = 10 ** file_size
            print(round_file_size)
            try:
                myDict[str(round_file_size)] += 1
            except KeyError:
                myDict[str(round_file_size)] = 1
    print(myDict)

# generate_files()
show_size()