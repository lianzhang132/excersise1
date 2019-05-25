import re

str1 = "15425651@qq.com sadfha@163.com sfsjge23adfd@fd.com.cn sdfefd@sina.com"
rel = "\w+@[0-9a-z]+(?:\.com|\.cn){1,2}"
print(re.findall(rel,str1))