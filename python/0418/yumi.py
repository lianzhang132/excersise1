
def con(n):
    if n == 0:
        return 1
    else :
        return 2*(con(n-1)+1)


print(con(10))



"""
n = 1
i = 0
for i in range(0,9):
    n = 2*n+1
    print(n)

"""