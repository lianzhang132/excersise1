set1 = {"dema","zhaoxin","jiela","jiuweiyaohu","shizigou","nuoke","jin"}
set2 = set(["shitou","zhaoxin","lanbo","ez","shizigou","hanbingsheshou","jin"])

# print(set1)
# print(set2)
#
# print(len(set1))
# print(max(set1))
# print(min(set1))
#
# set1.add("guafu")
# print(set1)
# set1.update(["shituren","datou"],["jianji"])
# print(set1)

# set2.pop()
# # 随机删除一个元素
# print(set2)
# set2.remove("dema")
# # 删除指定元素
# print(set2)
# set2.discard("shitouren")
# print(set2)
# set2.clear()
# print(set2)
# del set2
# print(set2)
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set2.symmetric_difference(set1))
print(set1.union(set2))
# set1.update(set2)
# print(set1)
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
