def mystery(x):
    a = [0, 4, 0, 3, 2]
    while x > 0:
        x = a[x]
    return "Done"
# Function runs forever when x=3 or when x=-2
