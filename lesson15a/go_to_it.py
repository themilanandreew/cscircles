def findLine(prog, target):
    for i in prog:
        if i[:i.index(" ")] == target:
            return prog.index(i)
