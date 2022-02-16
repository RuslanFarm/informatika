j = ''
s = 6
n = 1
for x in range(0, 30000, 1):
    while s * (x // 15) < 300:
        x += 1
        s += 18
        n *= 2
    if n <= 500:
        print(n)


