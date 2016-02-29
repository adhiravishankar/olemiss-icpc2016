r = lambda: map(int, input().strip().split(' '))
n, k = r()
maxpass = 1
minfail = k
for i in range(n):
    f, s = input().strip().split(' ')
    f = int(f)
    val = s == "SAFE"
    if val and f > maxpass:
        maxpass = f
    elif not val and f < minfail:
        minfail = f

print(maxpass+1, minfail-1)
