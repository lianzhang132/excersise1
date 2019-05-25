year = int(input("请输入查询年分"))


if year%4==0 or year%100!=0 :
    if year%400==0:
        print("这是一个世纪润年，去纪念一下吧")
    else:
        print("这是一个普通闰年")

else:
    print("这就是一个平年")