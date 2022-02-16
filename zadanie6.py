count=0
for i in range(0, 30000, 1):
    x=i
    s=6*(x//15)
    n=1
    while s < 300:

        s += 18
        n *= 2
    if 2 <= n <= 500:
        count+=1
print(count)


