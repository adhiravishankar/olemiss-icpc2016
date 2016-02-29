from collections import Counter

s = input().strip()
count = Counter(s)
l = len(count)
d = 0 if l <= 2 else 1 if l == 3 else l - 2
maxChar = list(map(lambda p: p[1], count.most_common(2)))
print(len(s) - sum(maxChar))
