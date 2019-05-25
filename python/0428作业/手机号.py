import re
str1 ="""24458645416 
13245879594 15485awe546 
11269656955 
17761667980"""
rel = "^1[3-9][0-9]{9}"
print(re.findall(rel,str1,re.M))