def prod(L):
    prod = 1
    for i in range(0, len(L)):
        prod *= L[i]
    return prod
