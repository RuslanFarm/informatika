def N_in_6(n):
    s = ''
    while n != 0:
        s += str(n % 6)
        n //= 6
    s = int(s[::-1] + s[0])
    print(s)
    s2 = (bin(s) + bin(s)[-1])[2:]
    print(s2)

    s3 = ''
    while s2 != 0:
        s3 += str(s2 % 10)
        s2 //= 10
    s3 = int(s3[::-1] + s3[0])
    print(s3)


N_in_6(13)
