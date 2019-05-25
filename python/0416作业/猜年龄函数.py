
def cai(age):
    i = 1
    age0 = 18
    while i <= 3:
        age = int(input("请输入您猜想的年龄"))
        if age < age0:
            print("我没这么年轻哦，在才一次吧")
        elif age > age0:
            print("我年龄太大了 吧 ，再来一次吧。")

        else:
            print("恭喜您 猜对了哦")
            break
        i += 1
cai(20)
