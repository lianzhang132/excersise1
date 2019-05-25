scor1 = input("请输入你的分数")

scor = int(scor1)

if scor>=90 and scor<=100:
    print("优秀")

elif scor>=80 and scor<90:
    print("良好")
elif scor >= 70 and scor < 80:
    print("还可以")
elif scor>=60 and scor<70:
    print("及格")
else:
    print("真差")