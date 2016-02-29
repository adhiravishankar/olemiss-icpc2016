from collections import deque

def ints():
    return list(map(int, input().strip().split(' ')))

class State:
    def __init__(self, position, generation):
        self.position = position
        self.generation = generation

height, width = ints()

grid = []
for i in range(width):
    grid.append([0] * height)

for i in range(height):
    s = input().strip()
    for j in range(width):
        grid[j][i] = int(s[j])

queue1 = deque()
queue1.append(State((0, 0), 0))
queue2 = deque()
queue2.append(State((width - 1, height - 1), 0))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

hits1 = {}
hits2 = {}

def step(cur, queue, our_hits, other_hits):
    if cur.position in other_hits:
        print(cur.generation + other_hits[cur.position])
        exit()
    else:
        for (dx, dy) in directions:
            k = grid[cur.position[0]][cur.position[1]]
            if k is 0:
                continue
            candidate = (cur.position[0] + (dx * k),
                         cur.position[1] + (dy * k))
            if candidate[0] >= 0 and candidate[0] < width and candidate[1] >= 0 and candidate[1] < height:
                our_hits[candidate] = cur.generation + 1
                queue.append(State(candidate, cur.generation + 1))

while len(queue1) is not 0 and len(queue2) is not 0:
    step(queue1.popleft(), queue1, hits1, hits2)
    step(queue2.popleft(), queue2, hits2, hits1)
else:
    print(-1)
