from math import floor, sqrt


def isItPrime(n):
    if n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = floor(sqrt(n))
        i = 5
        while i <= r:
            if n % i == 0:
                return False
            if n % (i + 2) == 0:
                return False
            i += 6
        return True


def genPrime():
    isPrime = [False, False, True]
    for i in range(3, 1000001, 2):
        isPrime.append(isItPrime(i))
        isPrime.append(False)
    return isPrime


isPrime = genPrime()
