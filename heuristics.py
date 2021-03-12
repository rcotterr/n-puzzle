import config


def manhattan_distance(current, final):
    n = config.N
    sum_ = 0
    for ind_cur, val in enumerate(current):
        ind_final = final.index(val)
        row_cur = ind_cur // n
        row_final = ind_final // n
        column_cur = ind_cur % n
        column_final = ind_final % n
        dist = abs(row_cur - row_final) + abs(column_cur - column_final)
        sum_ += dist
    return sum_


def linear_conflict(current, final):
    n = config.N
    sum_ = manhattan_distance(current, final)
    length = len(current)
    i = 0
    while i < length:
        start_row = i
        finish_row = i + n
        row = i // n
        while i // n == row:
            num1 = current[i]
            final_ind_num1 = final.index(num1)
            if not (ord(num1) and row == final_ind_num1 // n):
                i += 1
                continue
            j = i + 1
            while j < finish_row:
                num2 = current[j]
                final_ind_num2 = final.index(num2)
                if start_row <= final_ind_num2 < finish_row and final_ind_num2 < final_ind_num1 and ord(num2):
                    sum_ += 2
                j += 1
            i += 1
    return sum_


def corner_conflict(current, final):
    n = config.N
    sum_ = manhattan_distance(current, final)
    ind_corners = [0, n - 1, n * n - n, n * n - 1]
    for ind in ind_corners:
        if current[ind] != final[ind] and ord(current[ind]):
            neigh1 = ind - 1 if ind % n != 0 else ind + 1
            neigh2 = ind - n if ind // n != 0 else ind + n
            if current[neigh1] == final[neigh1] or current[neigh2] == final[neigh2]:
                sum_ += 2
    return sum_


def uniform_cost(_, __):
    return 0
