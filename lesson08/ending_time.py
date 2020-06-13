t1 = input()
d = int(input())
h = int(t1[0:2])
m = int(t1[3:5])
if d + m > 59:
    h = h + (d + m) // 60
    m = (d + m) % 60
    if len(str(m)) == 1:
        m = '0' + str(m)
    if h > 23:
        h = h % 24
        if len(str(h)) == 1:
            h = '0' + str(h)
print(str(h) + ':' + str(m))
