from final_state import final_state
from a_star import a_star
from read import read
from heuristics import manhattan_distance, linear_conflict, corner_conflict, uniform_cost
from check_solvable import is_solvable
import sys
import config


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 1:
        print('usage: python3 main.py [-h1/-h2/-h3/-u/-g] file\n-h1: A-star with a manhattan distance heuristic'
              '\n-h2: A-star with a linear conflict in row heuristic\n-h3: A-star with a corner conflict heuristic\n'
              '-u: a uniform cost search\n-g: a greedy search')
        exit()
    config.H = manhattan_distance
    for arg in argv:
        if arg == '-h2':
            config.H = linear_conflict
        elif arg == '-h3':
            config.H = corner_conflict
        elif arg == '-u':
            config.H = uniform_cost
        elif arg == '-g':
            config.STEP_G = 0
    try:
        char_start = read(argv[-1])
        char_final = final_state()
        if is_solvable(char_start, char_final):
            a_star(char_start, char_final)
        else:
            print("The puzzle is unsolvable")
    except Exception as exp:
        print('Something went wrong:', exp)
