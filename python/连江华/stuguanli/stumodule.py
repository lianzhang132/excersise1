import json
import os
from prettytable import PrettyTable

if os.path.isfile("info"):
    file1 = open("info","r")
    stu_li = json.load(file1)

else:
    stu_li = []


def stu_add():
    if len(stu_li)>0:
        last_stu = stu_li[-1]["sid"]
        sid = int(last_stu)+1
    else:
        sid =1
    file1.close()
    name1 = input("请输入姓名")
    age1 = input("请输入年龄")
    sex1 = input("请输入性别")
    sid = str(sid).rjust(5,"0")
    new_stu = {"sid":sid,"name":name1,"age":age1,"sex":sex1}
    stu_li.append(new_stu)
    stu_save()
def stu_save():
    file1 = open("info","w")
    json.dump(stu_li,file1)
    file1.close()
def stu_show(stu_li):
    pt = PrettyTable(["编号","姓名","年龄","性别"])
    pt.padding_width = 10
    for i, v  in enumerate(stu_li):
        pt.add_row(list(v.values()))
    print(pt)
def find_stu(key,reverse = False):
    global stu_li
    stu_li  = sorted(stu_li, key=lambda s: s[key], reverse=reverse)
    return stu_li
def ser_stu(key,my):
    ser_stuli =[]
    for stu in stu_li:
        if stu[key] ==my:
            ser_stuli.append( stu)
    return ser_stuli
def del_stu(d_stu):
    is_delete = False
    for n,value in enumerate(stu_li):
        if d_stu == value["sid"]:
            is_delete =True
            del stu_li[n]
    if is_delete==True:
        stu_save()
    stu_show(stu_li)
    return is_delete

def  stu_edit(sid,key,value):
    for n , stu in enumerate(stu_li):
        if sid ==stu["sid"]:
            stu_li[n][key] = value
    stu_save()

