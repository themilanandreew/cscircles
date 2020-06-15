list1 = [9, 1, 1]
list3 = list(list1)
list2 = list1
list4 = list3[:]
list1[0] = 4
list5 = list1
print(list1 is list2, list2 is list3, list3 is list4, list4 is list5)
print(list1 == list2, list2 == list3, list3 == list4, list4 == list5)
# Output: True False False False \n True False True False
