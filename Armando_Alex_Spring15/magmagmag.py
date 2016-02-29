n = int(input().strip())

for i in range(3 + (n % 2), n, 2):
    if n % i == 3:
        print(i)
        break
