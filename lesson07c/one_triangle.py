n = int(input())
for i in range(n-1, -1, -1):
    line = ''
    for j in range(-1, i):
        line += '1'
    print(line)
