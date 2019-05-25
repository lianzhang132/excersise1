import re
str1 = "192.168.1.1 1.0.0.0 128.15.26.5 224.5.26.89 240.48.52.12"
rel = "(?:[1-2][0-9]*[0-9]*\.)(?:[0-9][0-9]*[0-9]*\.){2}(?:[0-9][0-9]*[0-9]*)"
print(re.findall(rel,str1))
print(re.match(rel,str1))
ser = re.search(rel,str1)
print(ser)