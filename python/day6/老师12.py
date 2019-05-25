age = 10
n = 1
while True:
    if n>3:
        print('实际年龄是',age)
        break
    else:
        a = int(input("请输入年龄"))
        if a < age:
            print('输入的年龄小于实际年龄')
        if a > age:
            print('输入的年龄大于实际年龄')
        if a == age:
            print("恭喜你年龄猜对了")
            break
    n+=1