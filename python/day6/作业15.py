n = 100000
a =0

while n >=1000:
    if n >=50000:
        n-=0.05*n
    else:
        n-=1000



    a+=1
    print("第%d次经过路口，剩余%d钱"%(a,n))
