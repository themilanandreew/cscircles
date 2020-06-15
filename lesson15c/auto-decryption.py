# Variable letterGoodness is predefined


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


def spy_decoder(string, shift):
    return spy_coder(string, -shift)


def goodness(string):
    count = 0
    for i in string:
        if i != ' ':
            count += letterGoodness[ord(i) - 65]
    return count


strinput = input()
highg = 0
highs = 0
for i in range(0, 25):
    if goodness(spy_decoder(strinput, i)) > highg:
        highg = goodness(spy_decoder(strinput, i))
        highs = i
print(spy_decoder(strinput, highs))
