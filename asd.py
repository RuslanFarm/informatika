def N_in_6(n):
    s = ''
    while n != 0:
        s += str(n % 6)
        n //= 6
    s = int((s[::-1] + s[0]), 6)
    # s=int(s,6)
    s2 = (bin(s) + bin(s)[-1])[2:]
    # s3 = int((s3[::-1] + s3[0]), 2)
    return int(s2, 2)


# N_in_6(13)
for i in range(1, 1000):
    f = N_in_6(i)
    if f < 344:
        print(f)
