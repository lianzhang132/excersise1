import math
def circol(r):
    d  = 2*r*math.pi
    s = float(math.pi*r*r)
    # print("这个圆的周长是%d"%(d))
    print("这个圆的面积是%d"%(s))
    return round(d ,2),round(s,2)
circol(5)