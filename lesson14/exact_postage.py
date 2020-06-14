def postalValidate(S):
    S = S.replace(" ", "")
    if len(S) == 6 and (S[0]+S[2]+S[4]).isalpha() and \
            (S[1]+S[3]+S[5]).isdigit():
        return S.upper()
    return False
