n = input().strip()
count = 0
while len(n) > 1:
    p = 1
    for i in n:
        p *= int(i)
    n = str(p)
    count += 1
print(count)
