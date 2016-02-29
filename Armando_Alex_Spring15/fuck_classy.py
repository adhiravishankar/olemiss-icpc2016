class Classes:
    def __init__(self, modifiers):
        self._modifiers = modifiers

    def __repr__(self):
        return str(self._modifiers)

    def _getFromModifiers(self, n):
        if n >= len(self._modifiers):
            return 0
        else:
            return self._modifiers[n]

    def __eq__(self, other):
        for i in range(max(len(self._modifiers), len(other._modifiers))):
            if self._getFromModifiers(i) != other._getFromModifiers(i):
                return False
        else:
            return True

    def __lt__(self, other):
        for i in range(max(len(self._modifiers), len(other._modifiers))):
            if self._getFromModifiers(i) < other._getFromModifiers(i):
                return True
            elif self._getFromModifiers(i) > other._getFromModifiers(i):
                return False
        else:
            return False

count = int(input())
pairs = []

classMap = {'upper': -1, 'middle': 0, 'lower': 1}

for i in range(count):
    name, rest = input().strip().split(': ')
    classes = list(map(classMap.get, rest.split(' ')[:-1]))
    classes.reverse()

    pairs.append((Classes(classes), name))

for (_, name) in sorted(pairs):
    print(name)
