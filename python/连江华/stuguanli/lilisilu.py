while True:
    print("""
           # 请输入需要修改的选项
           #         [1]编辑学员 [2]删除学员 [3]返回上级菜单 [0]退出系统
           #             """)
    op3 = input("请输入操作菜单")
    if op3 == "1":
        if len(ser_stuli) > 1:
            sid = input("请输入要编辑学员的编号")
            print("""
                                       [1]编辑姓名
                                       [2]编辑年龄

                                       """)
            op4 = input("请输入您要操作的属性")
            if op4 == "1":
                name = input("请输入学员姓名")
                stu.stu_edit(sid, "name", name)
            elif op4 == "2":
                age = input("请输入学员年龄")
                stu.stu_edit(sid, "age", age)
            print("修改成功")
            stu.stu_show(ser_stuli("sid", sid))
        else:
            sid = ser_stuli[0]["sid"]
            print("""
                   [1]编辑姓名
                   [2]编辑年龄

                   """)
            op4 = input("请输入您要操作的属性")
            if op4 == "1":
                name = input("请输入学员姓名")
                stu.stu_edit(sid, "name", name)
            elif op4 == "2":
                age = input("请输入学员年龄")
                stu.stu_edit(sid, "age", age)
            print("修改成功")
            stu.stu_show(ser_stuli("sid", sid))
    if op3 == "2":
        # 删除用户
        if len(ser_stuli) > 1:
            sid = input("请输入学员编号")
        else:
            sid = ser_stuli[0]["sid"]
        ans = input("您确定要删除" + str(sid) + "号学员吗？【yes】是 【no】否")
        d_stu = sid
        if ans.lower() == "yes":
            res = stu.del_stu(sid)
            if res == True:
                print("删除成功")
            else:
                print("删除的学员不存在 ，【1】返回上一级【0退出系统】")
                op4 = input("请输入操作")
                if op4 == "1":
                    break
                else:
                    print("bye bye;;;;;")
                    exit()
        else:
            continue
    elif op3 == "3":
        break
    elif op3 == "0":
        print("bye bye;;;;;")
        exit()