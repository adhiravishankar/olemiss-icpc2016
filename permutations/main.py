from random import randint
import sys
import time

from perm_gen import heaps_r, heaps_i, jt, naive, builtin
from tsp import brute_force


def time_tsp(cities, solve_method, perm_method):
    print('Solving with', solve_method.__doc__)
    print('Generating permutations with', perm_method.__doc__)

    start = time.clock()
    route, length = solve_method(cities, perm_method=perm_method)
    print('Shortest route is', route, 'with length', length)
    print('Done in', time.clock() - start, 'sec')


if __name__ == '__main__':
    num_cities = 3
    cities = {x: (randint(0, 1000), randint(0, 1000)) for x in range(num_cities)}

    for method in [heaps_r, heaps_i, jt, naive, builtin]:
        start = time.clock()
        for perm in method(num_cities):
            pass
        print(method.__doc__, ':', time.clock() - start)
    # time_tsp(cities, brute_force, heaps_r)
    # time_tsp(cities, brute_force, heaps_i)
    # time_tsp(cities, brute_force, jt)
    # time_tsp(cities, brute_force, naive)
    # time_tsp(cities, brute_force, builtin)

# 10
# 3
# 8
# 30
# 0.6
