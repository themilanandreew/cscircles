def choose(n, k):
    count = 1
    for i in range(n, n-k, -1):
        count = count * i
    for j in range(k, 0, -1):
        count = count // j
    return count
