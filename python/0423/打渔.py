import time
import math

nt = time.time()
time1 = time.strptime("2015-01-01","%Y-%m-%d")
time2 = time.mktime(time1)
a = math.ceil((nt-time2)/86400)
if a %5 >=0 and a %5<=3:
    print("今天打渔")
else:
    print("今天晒网")
b = a+366
if b %5 >=0 and b %5<=3:
    print("明年的今天打渔")
else:
    print("明年的今天晒网")