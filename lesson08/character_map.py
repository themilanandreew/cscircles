c1 = 32
for i in range(0, 12):
    r = ""
    if i % 2 == 0:
        r += "chr: "
    else:
        r += "asc: "
    for j in range(c1, c1+16):
        if i % 2 == 0:
            r += " " + chr(j) + "  "
        else:
            if j < 100:
                r += str(j) + "  "
            else:
                r += str(j) + " "
            c1 += 1
    print(r)
