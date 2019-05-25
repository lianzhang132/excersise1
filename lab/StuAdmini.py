import os
import json
from prettytable import PrettyTable

# 首页展示菜单
def menu():
    print('*'*30,'学员管理系统','*'*30)
    print('''    1.添加学员  
    2.查看学员列表   
    3.搜索学员  
    4.删除学员  
    0.退出系统''')
    print('*'*74)

# 判断学员文件是否存在
if os.path.exists('stu.txt'):
    # 如果存在，读取json字符串反序列化为原数据类型
    stu_file = open('stu.txt','r')
    stu_list = json.load(stu_file)
else:
    stu_list = []
# 定义一个写入并保存学员信息函数
def save():
    stu_file = open('stu.txt','w')
    json.dump(stu_list,stu_file)
# 添加学员信息
def add():
    name = input('请输入姓名：')
    age = input('请输入年龄：')
    sex = input('请输入性别：')

    # 学员编号采用6位的整数  000001 000002以此类推
    last_sid = 0 if len(stu_list) == 0 else int(stu_list[-1]['sid'])
    sid = last_sid + 1
    # 格工化为6位的整数
    sid = '%0.6d'%sid
    # 个人信息类表
    person_list = {'sid':sid,'name':name,'age':age,'sex':sex}

    # 添加到学员列表
    stu_list.append(person_list)
    # 写入文件
    save()
# 查看学员列表
def show(stu=stu_list):
    pt = PrettyTable(['学号', '姓名', '年龄', '性别'])
    pt.padding_width = 5
    for line in stu:
        pt.add_row(line.values())
    print(pt)

# 按姓名升序排列
def sort(key,reverse=False):
    show(sorted(stu_list,key=lambda s:s[key],reverse=reverse))
# 按指定条件搜索
def search(key,value):
    global search_list
    search_list = []
    for stu in stu_list:
        if stu[key] == value:
            search_list.append(stu)
    show(search_list)

#按指定条件进行修改
def modify(key,value,sid):
    for k,v in enumerate(stu_list):
        if v['sid'] == sid:
            stu_list[k][key]=value
    #写入文件
    save()

#根据sid删除学员
def delete(sid):
    for k,v in enumerate(stu_list):
        if v['sid']==sid:
            del stu_list[k]
    #写入文件
    save()




















