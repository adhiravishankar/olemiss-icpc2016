N = int(input().strip())
names = {}
keys = {"upper":-1, "middle":0, "lower":1}
maxlen = 0
for i in range(N):
    n, s = input().split(': ')
    s = s.split(' ')[:-1]
    l = len(s)

    s = reversed(list(s))
    s = map(lambda k: keys[k], s)
    s = list(s)
    if l > maxlen:
        maxlen = l
    names[n] = s

for n in names:
    if len(names[n]) < maxlen:
        names[n] = names[n] + [0]*(maxlen - len(names[n]))

print(names)
pairs = sorted([(names[n], n) for n in names])
for _, n in pairs:
    print(n)
