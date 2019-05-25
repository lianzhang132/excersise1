import datetime
import time
import calendar
# # print(time.strftime(%j))
# # help(datetime.timedelta)
list1 = calendar.mdays
list1 = list1+list1[1:9]
jishu  = []
for i in range(1,13):
    lis2 =  list1[i:i+8]
    sum1 = lis2[0]+lis2[1]+lis2[2]+lis2[3]+lis2[4]+lis2[5]+lis2[6]+lis2[7]
    jishu.append(sum1)
jishu[6]+=1
jishu[7]+=1
jishu[8]+=1
jishu[9]+=1
jishu[10]+=1
jishu[11]+=1
print(jishu)
dt = datetime.datetime.now()
dt1 = dt +datetime.timedelta(days=244+365)
print(dt1)



# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.today())