import stu
str1 ="学员管理系统"

print(str1.center(50,"◇"))
print(50*"▼")
stu1=stu.Student

while 1:
    op = input("""请输入选项 
     1 添加学员 
     2 查看学员列表 
     3 查询编辑删除学员信息 
     4 成绩管理系统
     0 退出系统
     """)
    if op == "1":
        while 1:
            name = input("请输入您要添加学生的姓名")
            age = input("请输入您要添加学生的年龄")
            sex = input("请输入您要添加学生的姓别")
            stu1.name = name
            stu1.age = age
            stu1.sex= sex
            stu1.add(name,age,sex)
            op1 = input("""
                       [1]继续添加
                       [2]返回上级菜单
                       [0]退出系统
                       """)
            if op1 =="2":
                continue
            if op1 =="0":
                exit()
    elif op == "2":
        print("""请输入查看规则
        1 姓名 升序
        2 姓名 降序
        3 年龄 升序
        4 年龄 降序
        5 返回上级
        0 退出系统
        """)
        while 1:
            op1 = input("请输入您的选择")
            if op1 == "1":
                stu.Student.show(stu.Student.find("name", False))
            elif op1 == "2":
                stu.Student.show(stu.Student.find("name", True))
            elif op1 == "3":
                stu.Student.show(stu.Student.find("age", False))
            elif op1 == "4":
                stu.Student.show(stu.Student.find("age", True))
            elif op1 == "5":
                break
            elif op1 == "0":
                exit()
            else:
                print("您的输入有误，请重新输入")
                break
            # stu.Student.show(stu.stu_info_li)

    elif op == "3":
        print("""请输入搜索规则
            1 学员编号 
            2 学员姓名
            3 返回上级
            0 退出系统
            """)
        while 1:
            op1 = input("请输入您的选择")
            if op1 == "1":
                num = input("输入学员编号")
                stu_up = stu.Student.serch("num", num)
                stu.Student.show(stu_up)
            elif op1 == "2":
                name = input("输入学员姓名")
                stu_up = stu.Student.serch("num", num)
                stu.Student.show(stu_up)
            elif op1 == "3":
                break
            elif op1 == "0":
                exit()
            print("""
                    1 编辑学员 
                    2 删除学员
                    3 返回上级
                    0 退出系统
                    """)
            while 1:
                op2 = input("请输入您的选择")
                if op2 =="1":
                    num = input("请输入您要编辑学生的编号")
                    key = input("请输入您要编辑学生的信息")
                    value = input("请输入您要编辑学生的信息值")
                    stu.Student.update(num,key,value)
                    print("修改成功")
                elif op2 == "2":
                    num = input("请输入您要删除学生的编号")
                    stu.Student.delete(num)
                elif op2 == "3":
                    break
                elif op2 == "0":
                    exit()

    elif op == "4":
        num = input("请输入您要删除学生的编号")
        stu.Student.delete(num)

    elif op == "5":
        pass
    elif op == "0":
        exit()
    else:
        print("输入有误，禁止操作")
        pass