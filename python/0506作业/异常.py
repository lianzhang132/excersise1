"""
class Person():
    name = "guanyu"
    age = 20
    def __init__(self,sex):
        if not isinstance(sex,int):
            raise TypeError("年龄请输入整数")
try:
    # print(Person.name)
    # print(yuna)
    # print(int("aa"))
    person1 = Person
    person1(1)
except AttributeError as e:
    print(e)
except IndentationError as e:
    print(e)
except NameError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("一切正常")
finally:
    print("完工")


"""
class MyException(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    raise MyException("类型错误")
except MyException as e:
    print(e)