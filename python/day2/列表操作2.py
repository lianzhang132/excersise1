list1 = [1,2,6,3.25,852,2]
list1.append(9)
print(list1)
list1.extend(list1)
print(list1)
list1.insert(2,8)
print(list1)
list1.remove(2)
print(list1)
del list1[3]
print(list1)
print(list1.pop(5))
# print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

list1.reverse()
print(list1)
print(4 in list1)
print(4 not in list1)


# list1.clear()
# print(list1)
# del list1
# print(list1)
