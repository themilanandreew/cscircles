poem = ""
while True:
    strinput = input()
    if strinput == "###":
        break
    poem += strinput + " "
poem = poem.lower()
poem = poem.split()
maxc = 0
maxi = ""
for i in poem:
    if poem.count(i) > maxc:
        maxi = i
        maxc = poem.count(i)
print(maxi)
