list1=["杜龙飞","敬金桥","连江华","王聪","原昊","付豪",\
      "李青松","林华建","王云鹏","张峰浩","管世洋","李宗辉","孙德勃","杨超","王江峰"]
print(list1[2:6])
print(list1[5:1:-1])
print(list1[5:])
print(list1[:1])


from collections.abc import Iterable
print(isinstance(list1,Iterable))
for i  in list1:
    print(i)
str1 = "afdasafdagsde"
for a,b in enumerate (str1):
    print(a,b)

dic1 = {"name":"jone","age":18,"study":"python"}
for key in dic1:
    print(key)

for value in dic1.values():

    print(value)

for key,value in dic1.items():
    print(key,value)