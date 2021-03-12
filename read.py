import config


def read(file):
    n = 0
    list_num = []
    with open(file, 'r', encoding='utf8') as file:
        for line in file:
            print(line, end='')
            if line.startswith('#'):
                continue
            if '#' in line:
                line = line[:line.find('#')]
            list_line = line.split()
            list_line = [value for value in list_line if value]
            if len(list_line) == 1:
                n = int(list_line[0])
                continue
            if len(list_line) == n:
                for item in list_line:
                    list_num.append(int(item))
        print('')
    n2 = n * n
    valid = True
    char_start = ''
    for item in list_num:
        char_item = chr(item)
        if not 0 <= item < n2 or char_item in char_start:
            valid = False
        char_start += char_item
    config.N = n
    if not len(char_start) == n * n or not valid:
        print('The puzzle is invalid')
        exit()
    return char_start
