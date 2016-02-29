import heapq as heap

arr = []
for i in range(int(input().strip())):
    s = ''.join(reversed(input().strip().upper()))
    heap.heappush(arr, s)

while len(arr) > 0:
    print(heap.heappop(arr))
