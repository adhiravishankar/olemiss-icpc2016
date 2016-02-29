import heapq

n = int(input().strip())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input().strip()))

arr = []
while len(heap) > 0:
    arr.append(heapq.heappop(heap))

vals = set()
for i in range(len(arr)//2):
    val = arr[i] + arr[len(arr)-i-1]
    vals.add(val)
print(min(vals))
