from math import cos, sqrt
length = float(input())
a = float(input())
for i in range(0, 10):
    print(length * cos(a * cos(i * sqrt(9.8/length))) - length * cos(a))
