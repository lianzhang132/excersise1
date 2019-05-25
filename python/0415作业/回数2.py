def huiwen1(n):
    c = 0 #计数
    huiwen =[]
    for i  in range(1,n+1):
        if str(i) == str(i)[::-1]:
            huiwen.append(i)
            c+=1
            # continue

    print(huiwen)
    print("共有%d个"%(c))


huiwen1(100)