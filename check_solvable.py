import config


def is_even_perm(sequence):
    my_count = 0
    for i, num in enumerate(sequence, start=1):
        my_count += sum(num > num2 for num2 in sequence[i:])
    return not my_count % 2


def defers_by_even_tr(char_start, char_final):
    ind_start = char_start.index(chr(0))
    ind_final = char_final.index(chr(0))
    n = config.N
    row_start = ind_start // n
    row_final = ind_final // n
    column_start = ind_start % n
    column_final = ind_final % n
    dist = abs(row_start - row_final) + abs(column_start - column_final)
    return not dist % 2


def is_solvable(char_start, char_final):
    parity_is_equal = is_even_perm(char_start) == is_even_perm(char_final)
    tr_n_even = defers_by_even_tr(char_start, char_final)
    if parity_is_equal:
        return tr_n_even
    else:
        return not tr_n_even
