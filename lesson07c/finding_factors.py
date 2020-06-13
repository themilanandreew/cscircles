n = int(input())
i = 1
while i <= n:
    if n % i == 0:
        print("{} times {} equals {}".format(i, n//i, n))
    i += 1
