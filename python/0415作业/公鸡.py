"""
假如 公鸡a 只 母鸡 b只 则小鸡 等于 100-a-b只

"""
a = 1

while a <= 100:
    b = 1
    while  b<= 100 :
        if 5*a+3*b+(100-a-b)/3 ==100:
            print("有公鸡%d只，有母鸡%d只，有小鸡%d只，"%(a,b,100-a-b))


        b += 1

    a+=1