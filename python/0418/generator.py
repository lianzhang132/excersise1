"""
ge1 = (i for i in range(0,10))
print(next(ge1))
print(next(ge1))
print(next(ge1))
print(next(ge1))
print(next(ge1))



def fide(ma):
    a,b = 0 ,1
    while a <=ma:
        yield a
        a,b = b,a+b

fide_a = fide(50)
print(next(fide_a))
print(next(fide_a))
print(next(fide_a))
print(next(fide_a))
print(next(fide_a))
print(next(fide_a))
print(next(fide_a))
"""
str1 = "adsdffg"
# print(next(str1))
print(next(iter(str1)))