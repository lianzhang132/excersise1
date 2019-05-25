import re
str1 = "lainzhyngh15 ERJEIfd45 12655462 fa3945&^&*%^*  fje_d12"

rel = "[a-zA-Z]\w{0,15}"
print(re.findall(rel,str1))
