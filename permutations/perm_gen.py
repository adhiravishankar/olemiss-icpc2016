from itertools import permutations

def heaps_r(count):
    """Heap's algorithm (recursive)"""
    def _heaps_r(n, perm):
        if n == 1:
            yield perm
        else:
            for i in range(n):
                yield from _heaps_r(n-1, perm)
                if n % 2 == 0:
                    swap = i
                else:
                    swap = 1
                perm[swap], perm[n-1] = perm[n-1], perm[swap]

    yield from _heaps_r(count, [x for x in range(count)])


def heaps_i(count):
    """Heap's algorithm (iterative)"""
    perm = [x for x in range(count)]
    idx = [0 for i in range(count)]
    i = 1
    while i < count:
        if idx[i] < i:
            swap = i % 2 * idx[i]
            perm[swap], perm[i] = perm[i], perm[swap]
            yield perm
            idx[i] += 1
            i = 1
        else:
            idx[i] = 0
            i += 1


def jt(count):
    """Johnson-Trotter (recursive)"""
    def _jt(n, p, pi, direction):
        if n >= len(p):
            yield p
        else:
            yield from _jt(n+1, p, pi, direction)

            for i in range(n):
                z = p[pi[n] + direction[n]]
                p[pi[n]] = z
                p[pi[n] + direction[n]] = n
                pi[z] = pi[n]
                pi[n] += direction[n]
                yield from _jt(n+1, p, pi, direction)

            direction[n] = -direction[n]

    p = [x for x in range(count)]
    pi = [x for x in range(count)]
    direction = [-1]*count
    yield from _jt(0, p, pi, direction)


def naive(count):
    """a naive approach (recursive)"""
    yield from _naive([], count)

def _naive(current, count):
    if len(current) == count:
        yield current
    else:
        for i in range(count):
            if i not in current:
                new_perm = list(current)
                new_perm.append(i)
                yield from _naive(new_perm, count)


def builtin(count):
    """the builtin iterools.permutations"""
    yield from permutations(range(count))
