temp = input()
if temp[-1] == 'F':
    print(str((float(temp[:-1])-32) * 5 / 9) + 'C')
else:
    print(str(float(temp[:-1])*9/5 + 32) + 'F')
