"""
返回递增整数
"""
q=0   #全局变量
def z():
    def x():
        global q     #引用全局变量
        q+=1
        return q
    return x
b=z()
print(b())
"""
m = 0
def jishu():
    def jia():
        global m
        m=m+1
        print(m)
    return jia

jia = jishu()
jia()
"""
import random
rate = random.randint(0,10)
print(rate)