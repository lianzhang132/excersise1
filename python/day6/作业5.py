n = 1
qishu = []
oushu = []

while n<=100:
    if n%2==0:
        oushu.append(n)

    else:
        qishu.append(n)

    n+=1

print(oushu)
print(qishu)
