class CLASS:
    def __init__(self, numlist):
        self.vals = numlist

    def __eq__(self, cl):
        return self.n == cl.n

    def __lt__(self, cl):
        return self.n < cl.n

    def __repr__(self):
        return str(self.n)

    def __str__(self):
        return str(self.n)

n = int(input())
names = {}
keys = {'lower':-1, 'middle':0, 'upper':1}
for i in range(n):
    s = input().strip().lower()
    s = s.split(': ')
    s[1] = s[1].split(' ')[:-1]
    s[1] = map(lambda w: keys[w], s[1])
    s[1] = list(reversed(list(s[1])))
    names[s[0]] = CLASS(s[1])


arr = [(names[k], k) for k in names]
print(sorted(arr))
for _, k in sorted(arr):
    print(k)

'''
names = {'lower': 1, 'middle': 5, 'upper': 9}

count = int(input().strip())

pairs = []

for i in range(count):
    name, rest = input().strip().split(': ')
    classes = rest.split(' ')[:-1]
    classes.reverse()

    n = 0

    for j in range(len(classes)):
        n += names[classes[j]] / (10 ** j)
    n += (5.0/9.0) / (10 ** (len(classes) - 1))
    pairs.append((-n, name))

print(pairs)

for (_, s) in sorted(pairs):
    print(s)
'''
