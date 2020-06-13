timbits = int(input())
cost = 0
nlarge = timbits // 40
timbits -= nlarge * 40
cost += nlarge * 6.19
nmedium = timbits // 20
timbits -= nmedium * 20
cost += nmedium * 3.39
nsmall = timbits // 10
timbits -= nsmall * 10
cost += nsmall * 1.99
cost += timbits * 0.2
print(cost)
