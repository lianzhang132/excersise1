import random
class  Lol:
    attack = 0
    def statt(self,enemy):
        enemy.health -=self.attack

class stron(Lol):
    name = "程咬金"
    attack = 25
    health = 1500
    avoidance = 2
class master(Lol):
    name = "狐狸"
    attack = 30
    health = 900
    avoidance = 4
class Game:
    def __init__(self,person1,person2):
        print(" game starting")
        self.hero1 = person1
        self.hero2 = person2
        print("*"*50)
        print("""
        %sVS%s
        [1]攻击
        [1]躲避
        """%(self.hero1.name,self.hero2.name))
    def fight(self):
        print("""
        %s血量%d      %s血量%d
        """%(self.hero1.name,self.hero1.health,self.hero2.name,self.hero2.health))
        op1 = input("请输入坦克的选择")
        op2 = input("请输入法师的选择")
        if op1 =="1":
            print("%s发起了攻击"%self.hero1.name)
            if op2=="1":
                print("%s发起了攻击"%self.hero2.name)
                self.hero1.statt(self.hero2)
                self.hero2.statt(self.hero1)
            else:
                print("%s发起了躲避" % self.hero2.name)
                num = random.randint(0,10)
                if num <= self.hero2.avoidance:
                    print("%s躲避成功"%self.hero2.name)
                else:
                    self.hero1.statt(self.hero2)
        else:
            print("%s发动了躲避"%self.hero1.name)
            if op2=="1":
                print("%s发起了攻击"%self.hero2.name)
                num = random.randint(0, 10)
                if num <= self.hero1.avoidance:
                    print("%s躲避成功" % self.hero1.name)
                else:
                    self.hero2.statt(self.hero1)

            else:
                print("%s发起了躲避" % self.hero1.name)
                print("%s躲避成功"%self.hero2.name)
    def v_f(self):
        if self.hero1.health>0 and self.hero2.health>0:
            is_v = False
        elif self.hero1.health<=0:
            print("%s挂了" % self.hero1.name)
            print("%s胜利" % self.hero2.name)
            is_v =True
        elif self.hero2.health<=0:
            print("%s挂了" % self.hero2.name)
            print("%s胜利" % self.hero1.name)
            is_v = True
        else:
            print("同归于尽")
            is_v = True
        return is_v


chengyaojin = stron()
daji = master()

game = Game(chengyaojin,daji)
while game.v_f() ==False:
    game.fight()
