class Girl:
    def __init__(self,name,age):

        self.name = name
        self.age = age
    def iage(self):
        print("送一枝花")


# girl1 =Girl
# attr = input("请输入属性")
# print(hasattr(girl1,"iage"))
# print(getattr(girl1,"age"))
# getattr(girl1,"iage")
# if hasattr(girl1,attr):
#     getattr(girl1, "iage")()
# else:
#     print("输入的属性不存在哦")
# setattr(girl1,"name","mairui")
# print(hasattr(girl1,"name"))
# delattr(girl1,"age")
# print(hasattr(girl1,"age"))
rose = Girl("Rose",22)
if hasattr(rose,"age"):
    print(getattr(rose,"age"))
    setattr(rose,"age",18)
    print(getattr(rose, "age"))
else:
    setattr(rose,"age",20)