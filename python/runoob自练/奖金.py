"""profit  = int(input("请输入当年利润"))
if profit>=100:
    jin = (profit-100)*0.01+(40*0.015)+20*(0.03+0.05)+10*(0.075+0.1)
    print("应发奖金%f万元"%(jin))
elif profit>=60 and  profit<100 :
    jin = (profit - 60) * 0.015 + 20 * (0.03 + 0.05) + 10 * (0.075 + 0.1)
    print("应发奖金%f万元" % (jin))
elif profit>=40 and  profit<60 :
    jin = (profit - 40) * 0.03 + 20 * 0.05 + 10 * (0.075 + 0.1)
    print("应发奖金%f万元" % (jin))
elif profit>=20 and  profit<40 :
    jin = (profit - 20) * 0.05 + 10 * (0.075 + 0.1)
    print("应发奖金%f万元" % (jin))
elif profit>=10 and  profit<20 :
    jin = (profit - 10) * 0.075 + 10 * 0.1
    print("应发奖金%f万元" % (jin))
else:
    jin = profit * 0.1
    print("应发奖金%f万元" % (jin))
"""
i = int(input("利润金额"))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range (0,6):
    if i >arr[idx]:
        r +=(i-arr[idx])*rat[idx]
        # print(i - arr[idx])*(int(rat[idx]))
        i = arr[idx]

print(r)