n = 2
sushu =[]
while n <=100:
    i =2
    while i <=n:
        if n%i==0:
            if n==i:
                sushu.append(n)
                # print(sushu)
            break


        i+=1



    n+=1


print(sushu)
# help (sum)