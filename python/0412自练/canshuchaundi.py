"""
num1 = 1

print(id(num1))
def shuzu():
    print(num1)
    print(id(num1))

shuzu()
print(id(num1))


num1 = [1,"iii"]

print(id(num1))
def shuzu():
    print(num1)
    num1.append(4)
    print(num1)
    print(id(num1))
shuzu()
"""

list1 = [1,2,3]
def ceshi(a):
    a.append(4)

ceshi(list1)
print(list1)

num1 = 1

def shuzu(m):
    m+=1
    print(num1)

shuzu(num1)
print(num1)
