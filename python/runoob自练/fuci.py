"""
def jia(a):
    return a+1

res = map(lambda x:jia(x),[1,2,3,4])
print(list(res))
"""
from functools import reduce
res = reduce(lambda a,b:a+b,[1,2,2,6,8,9])
print(res)

def is_qi(n):
    return n%2==1
new_li = filter(is_qi,[1,2,3,4,5,6,7,8,9,10])
print(list(new_li))
def a():
    c = 100
    def b():
        print(c)
    return b

sh = a()
sh()
