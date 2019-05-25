import time
time1 = time.localtime(time.time())
print(time1)
print(time.strftime("%Y-%m-%d %X"))
t2 = time.strptime("2018-10-2","%Y-%m-%d")
print(time.strftime("%j",t2))
a = [1,2,3]
b=a[:]
print(b)
for i in range(1,10):
    print(" ")
    for j in range(1,i+1):

        print ("%d * %d = %d   " %(j,i,i*j),end="")