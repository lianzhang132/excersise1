n = 100
shui = []

while n<=999 :
    a = n // 100
    b = (n - a * 100) // 10
    c = n - a * 100 - b * 10
    # print((a^3+b^3+c^3) is not n)
    if a**3+b**3+c**3 == n:
        shui.append(n)
    #     # print(a^3+b^3+c^3)
    #
    else:
        pass
    # #
    n+=1
print(shui)
