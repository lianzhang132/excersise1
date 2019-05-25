# class Roman:
#     u = n.index("I")
#     v = n.index("V")
#     x = n.index("X")
#     l = n.index("L")
#     c = n.index("C")
#     d = n.index("D")
#     f = n.index("M")

n = input("请输入罗马数字")
list1 = ["I","V","X","L","C","D","M"]
for i in n:
    if i not in list1:
        print("输入有误")

    else:
        li2 = list(n)

if    li2.index("C")<li2.index("M"):
    resu1 = (-li2.count("C") * 100) + li2.count("M") * 1000
    resu = li2.count("I") * 1 + li2.count("V") * 5 + li2.count("X") * 10 + li2.count("L") * 50 + \
             li2.count("D") * 500 + resu1
if li2.index("X") < li2.index("C"):
    resu1 = (li2.count("C") * 100) - li2.count("X") * 10
    resu = li2.count("I") * 1 + li2.count("V") * 5  + li2.count("L") * 50 + \
            li2.count("D") * 500 + li2.count("M") * 1000+resu1
if li2.index("I") < li2.index("V"):
    resu1 = (li2.count("V") * 5) - li2.count("I") * 1
    resu = resu1+ li2.count("X") * 10 + li2.count("L") * 50 + \
           li2.count("C") * 100 + li2.count("D") * 500 + li2.count("M") * 1000


if li2.index("I") < li2.index("V")< li2.index("X")< li2.index("L")< li2.index("C")< li2.index("D")< li2.index("M"):
    resu = li2.count("I")*1+li2.count("V")*5+li2.count("X")*10+li2.count("L")*50+\
               li2.count("C")*100+li2.count("D")*500+li2.count("M")*1000

print(resu)





# n = input("请输入罗马数字")
# luoma(n)