class Graph:
    def __init__(self):
        self.vset = set()
        self.data = {}

    def getvlabel(self, v):
        return self.data[v][0]

    def addVert(self, v, l):
        self.vset.add(v)
        self.data[v] = (l, set())

    def addEdge(self, v1, v2):
        self.data[v1][1].add(v2)

    def getNeighbors(self, v):
        return self.data[v][1]

r = lambda: map(int, list(input().strip()))

N, M = map(int, input().strip().split(' '))
graph = Graph()
for n in range(N):
    kvals = r()
    for m, k in zip(range(M), kvals):
        v = (n, m)
        graph.addVert(v, k)

for v in graph.vset:
    n, m = v
    k = graph.getvlabel(v)

    down = (n + k, m)
    right = (n, m + k)
    if down in graph.vset:
        graph.addEdge(down, v)
    if right in graph.vset:
        graph.addEdge(right, v)
