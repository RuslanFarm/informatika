s = ''
x = int(input())
a = 125 ** 200 - 5 ** x + 74
while a != 0:
    s += str(a % 5)
    a //= 5
s = s[::-1]
if s.count('4') == 100:
    print(x)
