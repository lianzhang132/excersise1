list1 = [1,2,6,3.25,852,2]

list2 = [
    [2,5,78,69],
    ["dema","zhaoxin","huangzi"]
]
print(len(list1))
print(max(list1))
print(min(list1))
print(list1[2])
print(list1.index(2))
print(list1.count(2))
list1[2] = 69
print(list1)
# print(list2)
list3 = list1.remove(69)
print(list1)
# print(del list2())
print(list1.append(9))