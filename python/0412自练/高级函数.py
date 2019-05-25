def abb(x ,y):
    print(x+y)

a = abb(1,2)
b = abb
print(id(abb),id(b))

b(10,20)