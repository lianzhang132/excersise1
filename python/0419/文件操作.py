file1 = open("test","r+",encoding ="utf-8")
print(file1.read())
file1.seek(2,0)
print(file1.read())
# print(file1.readline())
# print(file1.tell())
#
# # print(file1.seek(5,1))
# # print(file1.tell())
#
# print(file1.seek(10))
# print(file1.readline())
# # print(file1.tell())
# file1.write("开车需谨慎")
#
# print(file1.read())
#
# file1.writelines("absjfds")
#
# print(file1.read())
# file1.close()
#
# print(file1.read())