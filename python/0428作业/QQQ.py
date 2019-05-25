import re
str ="1072502827 2325770611 251268 12356 "
rel = "[0-9]{5}[0-9]{0,7}"
print(re.findall(rel,str))