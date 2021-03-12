from heapq import heappop, heappush
from find_neighbours import find_neighbours
from output import output
import config

F, G, H, STATE, PREV = range(5)


def a_star(char_start, char_final):
    closed = {}
    opened = []
    states = {}
    total_num_of_states = 0

    g = 0
    h = config.H(char_start, char_final)
    f = g + h
    start = [f, g, h, char_start, None]
    states[char_start] = start

    heappush(opened, start)
    max_states = len(states)
    while opened:
        if len(states) > max_states:
            max_states = len(states)
        x = heappop(opened)
        total_num_of_states += 1
        if x[STATE] == char_final:
            output(total_num_of_states, max_states, x, closed)
            return
        closed[x[STATE]] = x
        if x[STATE] not in states:
            continue
        del states[x[STATE]]
        list_neighbour_state = find_neighbours(x[STATE])
        for neigh_state in list_neighbour_state:
            if neigh_state in closed:
                continue
            neigh_node_g = x[G] + config.STEP_G
            if neigh_state in states:
                prev_g = states[neigh_state][G]
                if prev_g > neigh_node_g:
                    states[neigh_state][G] = neigh_node_g
                    states[neigh_state][F] = neigh_node_g
                    states[neigh_state][PREV] = x[STATE]
                    neigh_params = states[neigh_state]
                    heappush(opened, neigh_params)
            else:
                neigh_node_h = config.H(neigh_state, char_final)
                neigh_params = [neigh_node_g + neigh_node_h, neigh_node_g, neigh_node_h, neigh_state, x[STATE]]
                heappush(opened, neigh_params)
                states[neigh_state] = neigh_params
    print('The puzzle is unsolvable')
    return None
