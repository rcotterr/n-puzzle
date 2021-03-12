import config


def find_neighbours(char_state):
    n = config.N
    ind_zero = char_state.index(chr(0))
    list_neighs = []
    row = ind_zero // n
    column = ind_zero % n
    step = 1
    if row > 0:
        neigh_up = char_state[:ind_zero - n] + char_state[ind_zero] + char_state[ind_zero - n + 1:ind_zero] + \
                   char_state[ind_zero - n] + char_state[ind_zero + 1:]
        list_neighs.append(neigh_up)
    if row < n - 1:
        neigh_down = char_state[:ind_zero] + char_state[ind_zero + n] + char_state[ind_zero + 1:ind_zero + n] + \
                    char_state[ind_zero] + char_state[ind_zero + n + 1:]
        list_neighs.append(neigh_down)
    if column > 0:
        neigh_left = char_state[:ind_zero - step] + char_state[ind_zero] + char_state[ind_zero - step] + \
                     char_state[ind_zero + 1:]
        list_neighs.append(neigh_left)
    if column < n - 1:
        neigh_right = char_state[:ind_zero] + char_state[ind_zero + step] + char_state[ind_zero] + \
                     char_state[ind_zero + step + 1:]
        list_neighs.append(neigh_right)
    return list_neighs
