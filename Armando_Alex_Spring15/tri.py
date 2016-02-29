def ints():
    return list(map(int, input().strip().split(' ')))

first = sorted(ints())
second = sorted(ints())


def is_right(sides):
    a, b, c = sides
    return (a * a) + (b * b) == (c * c)

if first == second and is_right(first):
    print(1)
else:
    print(0)
