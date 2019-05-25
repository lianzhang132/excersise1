class we:
    print("fhds")
    class mn:
        print("wefcs")

te1= we
te2= we.mn
te1()
# te2()
if self.hero1.health > 0 and self.hero2.health > 0:
    is_v = False
elif self.hero1.health <= 0:
    print("%s挂了" % self.hero1.name)
    print("%s胜利" % self.hero2.name)
    is_v = True
elif self.hero2.health <= 0:
    print("%s挂了" % self.hero2.name)
    print("%s胜利" % self.hero1.name)
    is_v = True
else:
    print("同归于尽")
    is_v = True