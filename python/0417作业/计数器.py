"""
返回递增整数

"""

def jishu(n):
    n+=1
    def jia(m):
        m=m+1
        print(m)
    return jia

jia = jishu(2)
jia(2)