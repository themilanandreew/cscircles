x = "outer"


def xReplace(value):
    x = value


xReplace("inner")
print(x)

# Output: outer - local variable x is assigned to but never used
