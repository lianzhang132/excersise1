"""

1.变量a=3，b=8交换a和b值，至少3种方法实现？


a = 3
b = 8
a,b =b, a
print(a,b)

a = 3
b = 8
c = a
a = b
b = c

print(a,b)
"""
a = 3
b = 8
a = a+b
b =a-b
a =a-b

print(a,b)

"""

2.有一个字符串'abcdef',想得到 cd，3种方法实现？

"""
str1 = "abcdef"
print(str1[2:4])
print(str1[-4:-2])
print(str1[2:][0:2])

