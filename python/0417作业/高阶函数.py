"""
hidefun = lambda  a,b:a*b
print(hidefun(10,20))

def fun1(a,b):
    if a >= b:
        print(str(a)+" is the big number")
        return a
    else:
        print(str(b)+ " is the big number")
        return b

# writer(fun1(5,9))

res = map(lambda a: a+1,[2])
print(list(res))



from functools import reduce

def  writer(n,m):
    c = n+m
    return c

list1 = [1,32,5,9,8,7]

print(reduce(writer,list1))

"""
def bishu(n):
    ex = []
    if n >=80:
        ex.append(n)
    return ex
chengji = [("zhang",12),("lisi",8),("mayun",80),("mahauteng",89),("kini",52),("zhna",82),("dema",89)]
# list2 = list(filter(bishu,chengji))
# print(list2)
print(sorted(chengji,key=lambda s:s[1],reverse =True))