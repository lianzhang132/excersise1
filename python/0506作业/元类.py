# person = type("Person",(object,),{"name":"denma","age":18,"say":"hello"})
# print(person.say)
import re
"""
class PersonMetaclass(type):
    def __new__(cls, name,bases,attrs):
        if not re.match("[A-Z]\w*",name):
            print("请按大驼峰命名方式命名")

class Baf(object,metaclass=PersonMetaclass):
    pass

"""
class PersonMetaclass(type):
    def __new__(cls, name,bases,attrs):
        if "__doc__" not in attrs or len(attrs["__doc__"].strip())==0:
            print("类中请输入解释文档")

class Baf(object,metaclass=PersonMetaclass):
    """
    ahfhda

    """