def spy_coder(string, shift):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    out = ""
    for i in range(0, len(string)):
        if string[i] != ' ':
            if alpha.index(string[i]) + shift <= 25:
                out += alpha[alpha.index(string[i]) + shift]
            else:
                out += alpha[alpha.index(string[i]) + shift - 26]
        else:
            out += ' '
    return out


print("XUD HTIJW" == spy_coder("SPY CODER", 5))