year = int(input("请输入年"))
month = int(input("请输入月"))
date = int(input("请输入日期"))

mouths = (0,31,59,90,120,151,181,212,243,273,304,334)
if month>0 and month<=12:
    sum = mouths[month-1]
else:
    print("error")

sum += date
leap =0
if (year %400 ==0)or (year %4 ==0 and (year % 100 !=0)):
    leap =1
if (leap ==1 )and (month>2):
    sum +=1

print(sum)