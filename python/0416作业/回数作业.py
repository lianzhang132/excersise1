"""
1.	类似于 奶牛产牛奶、清水池里池水清、上海自来水来自海上 这样的语句称之为回文句
   类似于 1  11  101  12321  234432 这样的数称之为回文数
   要求：打印出1-n之间的所有回文数，并统计出总个数

转换列表 进行反转后同索引元素比较 
"""

def huiwen1(n):
    c = 0 #计数
    huiwen =[]
    for i  in range(1,n+1):
        j = str(i)#转换字符串 判断位数
        l = list(j)#转换列表 需要用到反转命令
        b = len(j)
        d = int(b/2)#需要整形才能计算
        e = l[0:d]
        l.reverse()
        l1 = l
        f = l1[0:d]

        if e == f:
            huiwen.append(i)
            c+=1
        #else:
        #    pass

    print(huiwen)
    print("共有%d个"%(c))


huiwen1(10000)