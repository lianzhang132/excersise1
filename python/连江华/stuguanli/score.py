import os
import json
import stumodule as stu
from prettytable import PrettyTable
if os.path.isfile("scorelist"):
    file1 = open("scorelist","r")
    sco_dict = json.load(file1)
    file1.close()

else:
    sco_dict = {}
def stu_sco():
    while 1:
        print("""
        1 添加成绩
        2 查看成绩列表
        3 搜索学员成绩
        0 退出成绩    
        """)
        op1 =input("请输入操作")
        if op1 =="1":
            add()
            print("添加成功")
            print("""
            1 继续添加
            2 返回上级菜单
            0 退出系统
            
            """)
            op2 = input("然后您的选择是")
            if op2 =="1":
                add()
                print("添加成功")
            elif op2 =="2":
                break
            elif op2 =="0":
                print("再见")
                exit()
        elif op1 =="2":
            sco_show(sco_li())
        elif op1 =="3":
            subj = input("请输入学科")
            # mysid =input("请输入学员编号")
            sco_show(ser_stu_sco(subj))
        elif op1 =="0":
            print("再见了您恁")
            exit()





def add():
    subje = input("请输入学科")
    scores = {}
    for v in stu.stu_li:
        score = input("编号"+str(v["sid"])+"学员"+v["name"]+"的成绩为：")
        scores[v["sid"]]= score

    sco_dict[subje] = scores
    sco_save()


def sco_save():
    file1 = open("scorelist","w")
    json.dump(sco_dict,file1)
    file1.close()

def sco_li():
    stu_stu_sco = []
    for v in stu.stu_li:
        score = {}
        score["sid"]= v["sid"]
        score["name"]= v["name"]
        for subject,scores in sco_dict.items():
            score[subject]=scores[v["sid"]]
        stu_stu_sco.append(score)

    return stu_stu_sco
def sco_show(score_list):
    head = ["编号","姓名"]
    head +=sco_dict.keys()
    pt =  PrettyTable(head)
    pt.padding_width = 10
    for i, v in enumerate(score_list):
        pt.add_row(list(v.values()))
    print(pt)

def ser_stu_sco(my):
    stu_scoli =[]
    for stu in sco_dict:
        if stu["subject"] ==my:
            stu_scoli.append(stu)
    return stu_scoli