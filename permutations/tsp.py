import math

def _distance(cityA, cityB):
    dY = cityA[1] - cityB[1]
    dX = cityA[0] - cityB[0]
    return int(math.sqrt(dX**2 + dY**2))

def brute_force(cities, perm_method):
    """brute force"""
    min_length = 2147483647
    shortest_route = ()
    for route in perm_method(len(cities)):
        route_length = 0
        for i in range(0, len(route)-1):
            route_length += _distance(cities[route[i]], cities[route[i+1]])
        if route_length < min_length:
            shortest_route = tuple(route)
            min_length = route_length
    return shortest_route, min_length
