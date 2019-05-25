import time
nt = time.localtime(time.time())

week =int(time.strftime("%w"))
def week_num():
    if week == 0:
        a =  "星期日"
    elif week ==1:
        a = "星期一"
    elif week ==2:
        a = "星期二"
    elif week ==3:
        a = "星期三"
    elif week ==4:
        a = "星期四"
    elif week ==5:
        a = "星期五"
    else:
        a = "星期六"
    return a
nt1 = time.strftime("%Y{}%m{}%d{} {} %H:%M:%S").format("年","月","日",week_num())
print(nt1)
