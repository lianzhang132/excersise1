import StuAdmini as sa
while True:
    sa.menu()
    choice1 = int(input('请输入要进行的操作：'))
    if choice1 not in range(0,5):
        int(input('请输入正确的操作：'))
    else:
        if choice1 == 1:
            while True:
                sa.add()
                print('添加成功！')
                print('[1] 继续添加     [2] 返回上级菜单    [0]退出系统 ')
                choice2 = int(input('请选择要进行的操作：'))
                if choice2 == 1:
                    continue
                elif choice2 == 2:
                    break
                elif choice2 == 0:
                    print('结束操作')
                    exit()
        elif choice1 == 2:
            sa.show()
            while True:
                print("\n[1] 按姓名升序排列(默认)     [2] 按姓名降序排列     [3]按年龄升序排列    [4]按年龄降序排列   [5] 返回上级菜单    [0]退出系统 ")
                choice2 = int(input('请输入要进行的操作：'))
                if choice2 == 1:
                    sa.sort('name')
                elif choice2 == 2:
                    sa.sort('name',reverse=True)
                elif choice2 == 3:
                    sa.sort('age')
                elif choice2 == 4:
                    sa.sort('age',reverse=True)
                elif choice2 == 5:
                    break
                elif choice2 == 0:
                    exit()
        elif choice1 ==3:
            print('\n [1] 根据学员编号搜索   [2] 根据学员姓名搜索   [3] 返回上级菜单   [0]退出系统')
            choice2 = int(input('请输入要进行的操作：'))
            while True:
                if choice2 == 1:
                    choice3 = input('请输入学员编号：')
                    sa.search('sid',choice3)
                elif choice2 == 2:
                    choice3 = input('请输入姓名：')
                    sa.search('name',choice3)
                elif choice2 ==3:
                    break
                elif choice2 == 0:
                    exit()
                else:
                    print("非法操作")
                    continue
                # 编辑操作
                print("\n [1]编辑学员 [2]删除学员 [3]返回上级菜单 [0]退出系统")
                choice4 = int(input('请输入你要进行的操作：'))
                while True:
                    if choice4 == 1:
                        if len(sa.search_list)>1:
                            sid = input('请输入学员编号：')
                        else:
                            sid = sa.search_list[0]['sid']
                        print('\n [1]修改姓名 [2]修改年龄 [3]修改性别 [4]返回上级菜单 [0]退出系统')
                        choice5 = int(input('请输入要进行的操作：'))
                        while True:
                            if choice5 == 1:
                                name = input('请输入姓名：')
                                sa.modify('name',name,sid)
                                sa.show(sa.search_list)
                                print('修改成功')
                                break
                            elif choice5 == 2:
                                age = int(input('请输入年龄：'))
                                sa.modify('age', age, sid)
                                sa.show(sa.search_list)
                                print('修改成功')
                                break
                            elif choice5 == 3:
                                sex = input('请输入性别：')
                                sa.modify('sex', sex, sid)
                                sa.show(sa.search_list)
                                print('修改成功')
                                break
                            elif choice5 == 4:
                                break
                            elif choice5 == 0:
                                exit()
                    elif choice4 == 2:
                        # 判断是否搜索出多个结果
                        if len(sa.search_list) > 1:
                            sid = input("请输入你要删除的学员编号:")
                        else:
                            sid = sa.search_list[0]['sid']
                        # 删除学员
                        answer = input("确认要删除%s? [Yes]删除  [No]取消:" % sid)
                        if answer.lower() == 'yes':
                            sa.delete(sid)
                            print("删除成功!")
                            break
                        elif answer.lower() == 'no':
                            break
                        else:
                            print('非法操作')
                            break
                    elif choice4 == 3:
                        break
                    elif choice4 == 0:
                        exit()
        elif choice1 == 4:
           pass
        elif choice1 == 0:
            exit()
