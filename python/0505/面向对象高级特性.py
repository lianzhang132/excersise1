class Gir:
    def __init__(self,age):
        if age >=30:
            age-=10
        self.__age = age

    def fg(self):
        return self.__age
    def sg(self,age):
        if age>=15 and age <= 25:
            print("送lisa一支玫瑰")
        print(self.age)
    def dg(self):
        del self.__age
    age = property(fg,sg)
girl1 = Gir(32)
print(girl1.age)
girl1.sg(18)
# girl1.dg()
print(girl1.age)
