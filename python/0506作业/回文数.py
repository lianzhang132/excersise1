
"""
#判断一个数是否是回文数
121 12321 0 -2 -121 不包括小数

要求使用两种方式写一个函数

"""
"""
def is_huiwen(num):
    if num.isdigit():
        str1 = str(num)
        if str1[::1] ==str1[::-1]:
            print("是")
        else:
            print("不是")
    else:
        print("输入有误")


def is_huiwen(num):
    if num.isdigit():
        str1 = str(num)
        num1 = len(str1)
        m = 0
        if num1==1:
            return None

        else:
            while m <int(num1/2):
                if str1[m] ==str1[num1-m-1]:
                    m+=1
                else:
                    return "不是"
    else:
        print("输入有误")
        return "不是"
num = input("请输入要判断数据")
def fanhui(a):
    if is_huiwen(num)==None:
        return "是"
    else:
        return "不是"
print(fanhui(is_huiwen(num)))
"""
n = input("请输入要判断数据")
def huishu(n):
    x = int(n)
    if x<0 or(x != 0 and x%10 ==0 ):
        return False
    x_rev = 0

    while x > x_rev:
        x_rev = x_rev * 10 + x % 10
        x //= 10

    # x = 1 x_rev = 12
    return x_rev == x or x_rev // 10 == x
print(huishu(12))

# if huishu(n):
#     print(n+'是回文数')
# else:
#     print(n+'不是回文数')
