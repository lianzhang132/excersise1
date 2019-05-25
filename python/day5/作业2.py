import random
list1 =[
    {"name":"杜龙飞","age":18,"tel":"123"},
    {"name":"付豪","age":18,"tel":"123"},
    {"name":"管世洋","age":18,"tel":"123"},
    {"name":"李青松","age":18,"tel":"123"},
    {"name":"李宗辉","age":18,"tel":"123"},
    {"name":"林华建","age":18,"tel":"123"},
    {"name":"原昊","age":18,"tel":"123"},
    {"name":"张峰浩","age":18,"tel":"123"},
    {"name":"敬金桥","age":18,"tel":"123"},
    {"name":"连江华","age":18,"tel":"123"},
    {"name":"孙德勃","age":18,"tel":"123"},
    {"name":"王聪","age":18,"tel":"123"},
    {"name":"王江锋","age":18,"tel":"123"},
    {"name":"杨超","age":18,"tel":"123"},
    {"name":"王云鹏","age":18,"tel":"123"},
]
# print(list1)
# print(list1[random.randint(0,14)],"真好吃")


str1 = "this is  a python ,python is best"


"""
list1 = list(str1)
a = list1.index("p")
list1.remove("p")
b = list1.index("p")+1
print(a,b)

print(str1.replace("p","@"))

"""
n = str1.find("p")
ce =[]
while n!= -1:
    ce.append(n)
    n =n+1
    n = str1.find("p",n)
print(ce)
