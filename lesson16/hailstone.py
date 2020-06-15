def hailstone(n):
    if n == 1:
        print(n)
    else:
        print(n)
        if n % 2 == 0:
            hailstone(n // 2)
        else:
            hailstone(3 * n + 1)
