def isPalindrome(S):
    for i in range(0, len(S)-1):
        if S[i] != S[len(S)-(1+i)]:
            return False
    return True
