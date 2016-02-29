import math

def sieve(m):
    blist = [True]*m
    blist[0] = False
    for i in range(1, m):
        if blist[i]:
            x = (i+1)*(i+1)-1
            for j in range(x, m, i+1):
                blist[j] = False

    zlist = zip(blist, range(m))
    flist = filter(lambda p: not p[0], zlist)
    plist = map(lambda p: p[1]+1, flist)
    return plist


n = int(input().strip())

plist = sieve(math.floor(math.sqrt(n-3)))
for p in plist:
    if (n - 3) % p == 0:
        print((n - 3) // p)
