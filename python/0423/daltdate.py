import time
import math
import datetime
import calendar
nt = time.time()
time1 = time.strptime("2019-08-01","%Y-%m-%d")
time2 = time.mktime(time1)
dott = time2-nt
# print(dott)
day = math.floor(dott/86400)
hou = math.floor((dott%86400)/3600)
mint = math.floor((dott%86400)%3600)/60
sec = math.floor((dott%86400)%60)%60
print("当期距2019年8月1日有%d天%d小时%d分%d秒"%(day,hou,mint,sec))
#################################################################################
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
# print(jishu)
dt = datetime.datetime.now()
dt1 = dt +datetime.timedelta(days=jishu[3]+365)
print("20个月后的日期是",end=" ")
print(dt1)


