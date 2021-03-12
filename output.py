import config
F, G, H, STATE, PREV = range(5)


def output(total_num_of_states, max_states, x, closed):
    n = config.N
    print('complexity in time: ', total_num_of_states)
    print('complexity in size: ', max_states)
    list_moves = [x[STATE]]
    while x[PREV]:
        list_moves.append(x[PREV])
        x = closed[x[PREV]]
    print('number of moves: ', len(list_moves) - 1)
    list_moves.reverse()
    w = len(str(n * n))
    ind_prev = -1
    for state in list_moves:
        ind_zero = state.index(chr(0))
        for ind, i in enumerate(state):
            if not ind % n:
                print('')
            if ind == ind_prev:
                print("\033[33m {}".format(str(ord(i)).rjust(w)), end=' ')
            elif ind == ind_zero:
                print("\033[36m {}".format(str(ord(i)).rjust(w)), end=' ')
            else:
                print("\033[37m {}".format(str(ord(i)).rjust(w)), end=' ')
        ind_prev = ind_zero
        print()
