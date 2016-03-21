import networkx as nx
import matplotlib.pyplot as plt
from random import randint
from itertools import permutations
from timeit import default_timer as timer


def build_graph(cities):

    G = nx.Graph()
    G.add_nodes_from(cities)

    '''
    Adding nodes with random distance between them
    '''

    for i in range(len(cities)-1):
        for x in range(i + 1, len(cities)):
            G.add_edge(cities[i], cities[x], dist=randint(0, 100))
    return G


def print_Graph(G, min_dist):

    print 'For the following graph: '
    pos = nx.get_edge_attributes(G,'dist')
    print pos
    print 'Shortest path is ' + str(min_dist[0]) + ' following the order'
    print min_dist[1]
    p = nx.circular_layout(G)
    nx.draw(G, p)
    nx.draw_networkx_edge_labels(G, p, edge_labels=pos)
    plt.show()
    plt.savefig('tslgraph.png')


def solve(graph, cities):

    min_dist = (1000000,())
    for perm in permutations(cities):
        distance = 0
        for i in range(len(perm)-1):
            distance += graph[perm[i]][perm[i+1]]['dist']
        if distance < min_dist[0]:
            min_dist = (distance, perm)

    return min_dist


if __name__ == "__main__":
    cities = [k for k in range(10)]
    start = timer()
    graph = build_graph(cities)
    print_Graph(graph, solve(graph, cities))
    end = timer()
    print 'Total time: ' + str(end - start)