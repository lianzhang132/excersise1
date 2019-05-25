#在下面列表寻找两个数 两数之和等于target 返回这两个数的下标
list2 = [1,3,11,5]

target = 4
#target=8 返回值[1,3]
#target=6 返回值[0,3]
# 方案一
"""
def numsum(list2,target):
    for i in list2:
        for j in list2:
            if i+j==target and  list2.index(i)!=list2.index(j):
                return [list2.index(i),list2.index(j)]
"""
#方案二
def numsum(list2,target):
    for i in list2:
        if target-i in list2 and list2.index(i)!=list2.index(target-i):
            return [list2.index(i),list2.index(target-i)]

print(numsum(list2,target))