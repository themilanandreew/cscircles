def func(list):
    list[0] = list[0] + list[1]
    list[1] = list[1] + list[0]


data = [3, 4]
func(data)
print(data[0]*data[1])
# Output: 77
