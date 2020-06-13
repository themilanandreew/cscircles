from math import ceil
width = int(input())
strinput = ""
toprint = ""
first = 0
while True:
    strinput = input()
    if strinput == "END":
        break
    elif first == 0:
        first = 1
        toprint += ceil((width-len(strinput))/2)*"." + strinput + \
            ((width-len(strinput))//2)*"."
    else:
        toprint += "\n" + ceil((width-len(strinput))/2)*"." + strinput + \
            ((width-len(strinput))//2)*"."
print(toprint)
