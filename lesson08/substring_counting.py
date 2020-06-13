str2 = input()
str1 = input()
occs = 0
for i in range(0, len(str1) - len(str2)+1):
    if str1[i:i+len(str2)] == str2:
        occs += 1
print(occs)
