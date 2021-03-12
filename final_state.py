import config


def final_state():
    n = config.N
    array = [['0'] * n for _ in range(n)]
    i = 0
    j = 0
    num = 1
    while num < n**2:
        array[i][j] = str(num)
        while j + 1 < n and array[i][j + 1] == '0':
            array[i][j] = str(num)
            num += 1
            j += 1
        while i + 1 < n and array[i + 1][j] == '0':
            array[i][j] = str(num)
            num += 1
            i += 1
        while j > 0 and array[i][j - 1] == '0':
            array[i][j] = str(num)
            num += 1
            j -= 1
        while i > 0 and array[i - 1][j] == '0':
            array[i][j] = str(num)
            num += 1
            i -= 1
    char_final = ''
    for item in array:
        for i in item:
            char_final += chr(int(i))
    return char_final
