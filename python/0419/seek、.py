file1 = open("test","a+",encoding="utf-8")
# print(file1.read())
file1.seek(3,0)
print(file1.read())