"""
假如 大和尚a 个 则小和尚 等于 100-a-b个

"""
a = 1

while a <= 100:
    if 3*a+(100-a)/3 ==100:
        print("有大和尚%d个，有小和尚%d个。"%(a,100-a))
    a+=1