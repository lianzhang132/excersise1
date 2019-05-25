"""
def stu_add():
    stu = []
    stu_li =[]
    name1 = input("请输入姓名")
    age1 = input("请输入年龄")
    sex1 = input("请输入性别")
    stu.append(name1)
    stu.append(age1)
    stu.append(sex1)
    stu_li.append(tuple(stu))
    return stu_li
print(stu_add())


import json
stu = []
stu_li = []
name1 = input("请输入姓名")
age1 = input("请输入年龄")
sex1 = input("请输入性别")
stu.append(name1)
stu.append(age1)
stu.append(sex1)
stu_li.append(tuple(stu))
# file = open("info","r+")0
# json.dump(stu_li,file)
print(stu_li)

"""
import os
import json
if os.path.isfile("info"):
    file1 = open("info","r+")
    stu_li = json.load(file1)

    if len(stu_li)>0:
        last_stu = stu_li[-1]["sid"]
        sid = int(last_stu)+1
    else:
        sid =1
    file1.close()
else:
    sid = 1
    stu_li = []

