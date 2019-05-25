import re
str1 = "412725199106126512 41525852855254892X"
rel = "4[0-9]{16}(?:[0-9]|X)"
print(re.findall(rel,str1))
res1 = re.search("(?P<provice>\d{3})(?P<city>\d{3})(?P<birthdy>\d{8})(?P<sort>\d{3})(?P<verfy>[0-9A-Z])",str1)
# print(res1.groups())
# print(res1.group())
print(res1.groupdict())