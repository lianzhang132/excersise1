"""
学员管理系统

1 添加学员（编号自动生成，姓名，年龄，性别）
	添加成功后显示子菜单
		[1]继续添加
		[2]返回上级菜单
		[0]退出系统

2 查看学员列表
	子菜单
		[1]按姓名升序排列（默认）
		[2]按姓名降序排列
		[3]按年龄升序排列
		[4]按年龄降序排列
		[5]返回上级菜单
		[0]退出系统 exit()

3 查询学员信息
	子菜单
		[1]根据姓名查找
		[2]根据编号查找
		[3]返回上级菜单
		[0]退出系统4


4 删除学员信息（根据学员编号删除）


"""
import stumodule as stu
import score

str1 ="学员管理系统"

print(str1.center(50,"◇"))
print(50*"▼")

op = input("""请输入选项 
 1 添加学员 
 2 查看学员列表 
 3 查询编辑删除学员信息 
 4 成绩管理系统
 0 退出系统
 """)
while True:
    if op =="1":
        stu.stu_add()
        # stu.stu_save()
        while True:
            num2 = input("""
                            [1]继续添加
                            [2]返回上级菜单
                            [0]退出系统
                            
                            """)
            if num2 =="1":
                stu.stu_add()
                stu.stu_save()
            elif num2 == "2":
                exit()
            elif num2 == "0":
                exit()
            else:
                print("您的输入有误")
    elif op =="2":
        while True:
            op1 = input("请输入排序规则")
            print("""
            [1]按姓名升序排列（默认）
            [2]按姓名降序排列
            [3]按年龄升序排列
            [4]按年龄降序排列
            [5]返回上级菜单
            [0]退出系统
            """)


            if op1 =="1":
                stu.stu_show(stu.find_stu("name",False))
            elif op1 =="2":
                stu.stu_show(stu.find_stu("name",True))
            elif op1 =="3":
                stu.stu_show(stu.find_stu("sid",False))
            elif op1 =="4":
                stu.stu_show(stu.find_stu("sid", True))
            elif op1 =="5":
                break
            else:
                print("您的输入有误，请重新输入")
    elif op =="3":
        while True:
            op2 = input("""请输入查询学员信息
            [1]根据姓名查找
            [2]根据编号查找
            [3]返回上级菜单
            [0]退出系统
            """)
            if op2 =="1":
                op3 = input("请输入姓名")
                ser_stuli = stu.ser_stu("name",op3)
                stu.stu_show(ser_stuli)

            elif op2 =="2":
                op3 = input("请输入编号")
                ser_stuli = stu.ser_stu("sid",op3)
                stu.stu_show(ser_stuli)

            elif op2 =="3":
                op3 = input("请输入年龄")
                ser_stuli = stu.ser_stu("age",op3)
                stu.stu_show(ser_stuli)

            elif op2 == "4":
                break
            elif op2 =="0":
                exit()
            else:
                print("您的输入有误，请重新输入")
            while 1:
                print("""请输入您要编辑的内容
            [1]编辑  [2]删除 [3]返回上一级菜单 [4]退出系统
                                        """)
                op4 = input("请输入下一步操作")
                if op4 =="1":
                    if len(ser_stuli)>1:
                        sid = input("请输入您要编辑学员的编号")
                    else:
                        sid = ser_stuli[0]["sid"]
                        print("咋回事")

                    print("""
                    [1]编辑姓名 [2]编辑年龄
                    
                    """)
                    op5 = input("请输入您要操作的信息")
                    if op5 =="1":
                        name = input("请输入姓名")
                        stu.stu_edit(sid,"name",name)
                    elif op5 == "2":
                        age = input("请输入年龄")
                        stu.stu_edit(sid, "age", age)
                    print("修改成功！！！")
                    stu.stu_show(stu.ser_stu("sid",sid))
                if op4 == "2":
                    if len(ser_stuli) > 1:
                        sid = input("请输入您要删除的学员的编号")
                    else:
                        sid = ser_stuli[0]["sid"]

                    ans = input("您确定要删除"+str(sid)+"号学员吗？ 【yes】是 【no】否")
                    if ans.lower() == "yes":
                        res = stu.del_stu(sid)
                        if res == True:
                            print("删除成功")
                        else:
                            print("您要删除的学员不存在，【1】返回上一级 【0】退出系统")
                            op5 = input("请选择")
                            if op5 =="1":
                                break
                            else:
                                print("再见")
                                exit()
                    else:
                        continue
                if op4 =="3":
                    break
                if op4 =="0":
                    print("再见")
                    exit()








    elif op =="4":
        score.stu_sco()
    elif op =="0":
        print("再见")
        exit()
    else:
        print("输入有误，禁止操作")
        pass