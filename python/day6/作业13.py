"""
n = 100
for a in range(1,101):
    for b in range(1,101):
        if a+b ==n:
            if a*3+b/3==100:
                print("有大和尚", a, "个")
                print("有小和尚", b, "个")
"""


d = 1
while d<=33:
    x = 100-d
    if (x % 3 == 0) and (d * 3 + x / 3 == 100):
        print('大和尚%d人，小和尚%d人'%(d,x))
    d+=1

