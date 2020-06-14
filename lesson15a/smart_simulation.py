# BASIC had control structures, so this doesn't really work, and besides,
# it's stupid... I actually had to look at the hint to see whether they
# really intended the task to be solved this way...
# And the variable findLine is predefined.


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
