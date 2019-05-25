"""
def fibo(n):
    a = 1
    b = 1

    for i in range(1,n+1):
        if i <= 2:
            n = a
        else:
            n = a+b
            a,b = b,n
    return n


print(fibo(9))


"""


def fifi(i):
    if  i <= 2:
        return 1
    else:
        return fifi(i-1)+fifi(i-2)

print(fifi(5))
