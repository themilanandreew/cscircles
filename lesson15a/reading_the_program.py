def getBASIC():
    basic = []
    strinput = ""
    while True:
        strinput = input()
        basic += [strinput]
        if strinput[-3:] == "END":
            break
    return basic
