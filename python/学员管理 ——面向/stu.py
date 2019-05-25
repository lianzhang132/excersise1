from prettytable import PrettyTable
import json
import os


size = os.path.getsize("info")

if size != 0:
    file1 = open("info", "r")
    stu_info_li = json.load(file1)
else:
    stu_info_li = []



class Student:
    name="zhang"
    age="s"
    sex="s1"

    def add(name,age,sex):
        if len(stu_info_li) > 0:
            last_stu = stu_info_li[-1]["num"]
            num = int(last_stu) + 1
        else:
            num = 1
        num = str(num).rjust(5, "0")
        stu_info = {"num":num,"name":name,"age":age,"sex":sex}
        stu_info_li.append(stu_info)
        file1 = open("info", "w")
        json.dump(stu_info_li, file1)
        file1.close()


    def show(stu_info_li):
        pt = PrettyTable(["编号", "姓名", "年龄", "性别"])
        pt.padding_width = 10
        for i, v in enumerate(stu_info_li):
            pt.add_row(list(v.values()))
        print(pt)

    def serch(key, my):
        ser_stuli = []
        for stu in stu_info_li:
            if stu[key] == my:
                ser_stuli.append(stu)
        return ser_stuli

    def find(key, reverse=False):
        global stu_info_li
        stu_info_li = sorted(stu_info_li, key=lambda s: s[key], reverse=reverse)
        return stu_info_li

    def update(key, my,value):
        for n, stu in enumerate(stu_info_li):
            if key == stu["num"]:
                stu_info_li[n][my] = value
        file1 = open("info", "w")
        json.dump(stu_info_li, file1)
        file1.close()

    def delete(d_stu):
        is_delete = False
        for n, value in enumerate(stu_info_li):
            if d_stu == value["num"]:
                is_delete = True
                del stu_info_li[n]
        if is_delete == True:
            file1 = open("info", "w")
            json.dump(stu_info_li, file1)
            file1.close()
            print("删除成功")
        return is_delete