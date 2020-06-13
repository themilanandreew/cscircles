from math import sqrt
n = int(input())
x = 0
i = 1
while (x < (sqrt(n)-1)**2):
    x = i**2
    i += 1
    print(x)
