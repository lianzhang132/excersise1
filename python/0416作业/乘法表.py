def chengfa(m):
    for i in range(1,m+1):
        n = 1
        for n in range(1,i+1):
            print(str(n) + "*" + str(i) + "=" + str(i * n), end=" ")

        print(" ")
        
chengfa(12)
