n = 2
zhishu = []

while n<=100:
    i = 2
    # print(i)
    while i<=n:
        if n%i==0:
            if n==i:
                zhishu.append(n)
            break
        i+=1
    n+=1


print(zhishu)

