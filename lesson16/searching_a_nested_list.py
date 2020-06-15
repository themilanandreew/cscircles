def nestedListContains(NL, target):
    if type(NL) is list and target in NL:
        return True
    out = False
    for i in NL:
        if type(i) is list and nestedListContains(i, target):
            out = True
    return out
