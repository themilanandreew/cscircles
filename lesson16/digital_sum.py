def digitalSum(n):
    if n < 10:
        return n
    else:
        return n % 10 + digitalSum(n//10)
