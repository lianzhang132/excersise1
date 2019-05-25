tup1 = ("5","2",8,"9","1",[5,9])
tup2 = "a","b","c","d","e"
print(type(tup1))
print(type(tup2))
# 元组中的元素不可修改
str1 = tup1[2]
print(str1)
print(type(str1))


list1 = tup1[5]
print(list1)
list1[0] = 6
list1[1] = 10
# 元组中的元素包含列表时 列表是可以修改其中包含的元素的
print(tup1)
