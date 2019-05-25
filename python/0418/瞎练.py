m = 0
for i in range(1,5):
    a =str(i)
    for j in range(1,5):
        b = str(j)
        for u in range(1,5):
            c = str(u)
            if(a!=b) and (a!=c) and (c!=b):
                print(a + b + c)
                m+=1


print(m)