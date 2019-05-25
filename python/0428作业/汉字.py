import re

str1 = "haha 南极 北极 一带一路 丝绸之路 联合国 安理会"
rel = "[\u4e00-\u9fa5]+"
print(re.findall(rel,str1))
print(re.match(rel,str1))
ser = re.search(rel,str1)
print(ser)