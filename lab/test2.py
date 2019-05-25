def way2(a):
    b=str(a)
    for c in range(0,len(b)//2+1):
        if b[c]==b[len(b)-c-1]:
            return   print('是回文数')
        else:
            return   print('不是回文数')


def is_huiwen(num):
    if num.isdigit():
        str1 = str(num)
        num1 = len(str1)
        m = 0
        if num1==1:
            return None

        else:
            while m <int(num1/2):
                if str1[m] ==str1[num1-m-1]:
                    m+=1
                else:
                    return "不是"
    else:
        print("输入有误")
        return "不是"
# num = input("请输入要判断数据")
def fanhui(a):
    if is_huiwen(num)==None:
        return "是"
    else:
        return "不是"
def num():
    n = input('请输入数字')
    i = 0
    while i<len(n):
        if n[i] !=n[-1-i]:
            print('不是回文数')
            break
        else:
            i+=1
    else:
        print('是回文数')
num()
# way2(1278921)