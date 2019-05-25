# def find_stu(stu_li):
stu_li =[   ("张飞","20","nan"),
            ("关于","21","nan"),
            ("貂蝉","20","女"),
            ("小乔","19","女"),


         ]
a = input("请输入排序方式")
if a == "1":
    sorted(stu_li,key=lambda s:s[0],reverse = False)
elif a == "2":
    sorted(stu_li,key=lambda s:s[0],reverse = True)
elif a == "3":
    sorted(stu_li,key=lambda s:s[1],reverse = False)
elif a == "4":
    sorted(stu_li,key=lambda s:s[1],reverse = True)
# elif a == "5":
#     return student
elif a == "0":
    exit()
else:
    sorted(stu_li,key=lambda s:s[0],reverse = False)
# return stu_li
print(stu_li)