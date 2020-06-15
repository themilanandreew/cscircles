def check(S):
    count = 0
    if len(S.split()) != 4 or S.count(" ") != 3:
        return False
    for i in S.split():
        if not i.isdigit() or len(i) != 4:
            return False
        for j in i:
            count += int(j)
    return count % 10 == 0
