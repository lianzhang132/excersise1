# import  math, weixin
#
# weixin.weixin(3)
"""
from random import randint
print(randint(1,10))


from weixin import addfr

addfr()

import sys
print(sys.path)
sys.path.append("ahh")
print(sys.path)

from  tabulate import tabulate


print(tabulate(list1,["姓名","年龄"," 爱好"],tablefmt="mediawiki"))
"""
from prettytable import PrettyTable
list1 = [["dema",15,"kata"],["mumu",18,"huonv"],["manzi",20,"hanbing"]]

le = PrettyTable(["姓名","年龄","爱好"])
le.padding_width = 5
for row in list1:
    le.add_row(row)

print(le)