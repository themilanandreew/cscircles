#WTF? HOW IS THIS A BASIC EMULATOR?
def getBASIC():
    basic = []
    strinput = ""
    while True:
        strinput = input()
        basic += [strinput]
        if strinput[-3:] == "END":
            break
    return basic


def findLine(prog, target):
    for i in prog:
        if i[:i.index(" ")] == target:
            return prog.index(i)


def execute(prog):
    location = 0
    oldlocations = []
    while True:
        if location == len(prog)-1:
            return "success"
        T = prog[location].split()[2]
        oldlocations += [location]
        location = findLine(prog, T)
        if location in oldlocations:
            return "infinite loop"


print(execute(getBASIC()))
