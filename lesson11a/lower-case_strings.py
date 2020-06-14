def lowerChar(char):
    if ord(char) >= 65 and ord(char) <= 90:
        return chr(ord(char)+32)
    return char


def lowerString(string):
    result = ""
    for i in range(0, len(string)):
        result += lowerChar(string[i])
    return result
