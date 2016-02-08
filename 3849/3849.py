binaries = []
results = []

while True:
    a = [int(i) for i in input().split()]
    if a[0] == 0:
        break
    start = a[3]
    last = start
    binary = str(bin(start)[2:])
    while len(binary) < 16:
        binary = "0" + binary
    binaries.append(binary)

    while True:
        r = (((a[0] * a[3]) + a[1]) % a[2])
        if r == start or r == last:
            break
        binary = str(bin(r)[2:])
        while len(binary) < 16:
            binary = "0" + binary
        binaries.append(binary)
        a[3] = r
        last = r

    m = []
    for x in range (0, 16):
        zero = False
        one = False
        for questions in binaries:
            if questions[x] == '0':
                zero = True
            else:
                one = True

        if zero and one:
            m.append('?')
        else:
            if zero:
                m.append('0')
            else:
                m.append('1')

    print(''.join(m))
