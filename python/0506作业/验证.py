
"""ef is_huiwen(num):
    if num.isdigit():
        str1 = str(num)
        num1 = len(str1)
        m = 0
        if num1==1:
            return "是"

        elif num1>1:
            for m in range(0,int(num1/2)+1):
                if str1[m] ==str1[num1-m-1]:
                    m+=1
                return "是"
            else:
                return "不是"
    else:
        print("输入有误")
        return "不是"
num = input("请输入要判断数据")
# def fanhui(a):
#     if is_huiwen(num)==None:
#         return "是"
#     else:
#         return "不是"
# print(fanhui(is_huiwen(num)))
print(is_huiwen(num))

print(type(range(10)))
class Solution:
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b

    def aplusb(self,a,b):
        # write your code here
        return a+b
print(Solution.aplusb(1,2,3))
"""


class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    # def trailingZeros(self, n):
    #     # write your code here, try to do it without arithmetic operators.
    #     sum = 1
    #
    #     while n != 1:
    #         sum = sum * n
    #         n -= 1
    #     return sum
        # m = 0
        # while sum%10 == 0:
        #     sum = sum/10
        #     m += 1
        # return m

#
# print(Solution.trailingZeros(1, 30))
print(2//10)
# n=12521
# while n:
#     print(n//10)
#     n//=10
