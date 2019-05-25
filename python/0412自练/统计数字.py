"""
3. 统计数字
中文English
计算数字 k 在 0 到 n 中的出现的次数，k 可能是 0~9 的一个值。

"""
list1 = []
def count(m,n):

    for i in range(0,n+1):
        str1 = str(i)
        for val in str1:
            list1.append(val)
    cou1 = list1.count(str(m))
    return cou1

print(count(1,1))