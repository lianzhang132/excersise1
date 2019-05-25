money = 100000
i = 1
while money >= 1000:
    if money>50000:
            money = money - money * 0.05
    else:
        money = money - 1000
    print("第%d次,剩余%d钱"%(i,money))
    i+=1