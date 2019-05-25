import random

class weapon:
    #武器类：模型，血量，攻击，回避，被动,key
    def __init__(self,model,blood,atk,avoid,passive,price,key):
        self.model = model
        self.blood = blood
        self.atk = atk
        self.avoid = avoid
        self.passive = passive
        self.price = price
        self.key = key


class skill:
    #技能类：模型，血量，攻击，回避，类型，key
    def __init__(self,model,blood,atk,avoid,blue,type,key):
        self.model = model
        self.blood = blood
        self.atk = atk
        self.avoid = avoid
        self.blue = blue
        self.type = type
        self.key = key


class soldier:
    money = 200

    key = 1
    def __init__(self,type,name,blood,atk,avoid,blue):
        self.type = type
        self.name = name
        self.max_blood = blood
        self.blood = blood
        self.s_atk = atk
        self.base_atk = atk
        self.s_avoid = avoid
        self.base_avoid = avoid
        self.max_blue = blue
        self.blue = blue
        self.skill = []
        self.weapon = []

    #普通攻击
    def attack(self,other):
        print('{}攻击了{}，{}减去{}的血量------{}血量：{}  蓝：{}'.format(self.name,other.name,other.name,self.base_atk,self.name,self.blood,self.blue))
        return self.base_atk

    #使用技能
    def use_skill(self,other,skill):
        if skill.type == '主动':
            self.use_skill_z(skill)
            print('{}使用技能{}攻击了{}，{}减去{}的血量------{}血量：{}  蓝量：{}'.format(self.name,skill.model,other.name, other.name, self.s_atk, self.name,self.blood, self.blue))
            return self.s_atk
        elif skill.type == '被动':
            self.use_skill_b(skill)
    #使用被动
    def use_skill_b(self,skill):
        if skill.model == '浴血奋战':
            self.s_atk += (self.max_blood - self.blood)//10
            print('{}使用了【浴血奋战】----{}的战斗力：{}'.format(self.name,self.name,self.s_atk))
        elif skill.model == '亢奋':
            self.blood += 20 * self.key
            print('{}使用了【亢奋】----{}的血量:{}'.format(self.name, self.name,self.blood))
    #使用主动
    def use_skill_z(self,skill):
        #奋力一击----blue减2 -----攻击*2
        if skill.model == '奋力一击':
            self.blue -= 2
            self.s_atk *= 2
            print('{}使用了【奋力一击】----{}的蓝量：{},血量：{},战斗力：{}'.format(self.name,self.name, self.blue,self.blood,self.s_atk))
        #横扫千军----blue减2----攻击*3
        elif skill.model == '横扫千军':
            self.blue -= 2
            self.s_atk *= 3
            print('{}使用了【横扫千军】----{}的蓝量:{},血量：{},战斗力:{}'.format(self.name, self.name,self.blue,self.blue, self.s_atk))
        #天魔降世----blue减5----（需要购买方天画戟）----攻击*3，回避 = 50%，被动*2
        elif skill.model == '天魔降世':
            if '方天画戟' in self.skill:
                if self.blue >= skill.blue:
                    self.blue -= skill.blue
                    self.s_atk *= skill.atk
                    self.s_avoid = skill.avoid
                    self.key = skill.key
                    print('啊！啊！啊！世间万物以我为尊！！！\n{}使用了【天魔降世】----{}蓝量剩余：{},战斗力：{},血量：{},闪避：{}'.format(self.name, self.name,self.blue, self.s_atk,self.blood,self.s_avoid))
                else:
                    print('缺少蓝！！！')
            else:
                print('无法使用，请购买:方天画戟!!!')
        #凶兽出笼----           （blood <= 100） ----攻击*3，回血300
        elif skill.model == '凶兽出笼':
            if self.blood <= 100:
                if self.blue >= skill.blue:
                    self.blue -= skill.blue
                    self.s_atk *= skill.atk
                    self.blood += skill.blood
                    print('觉醒吧！我沉睡的灵魂！！！\n{}使用了【天魔降世】----{}蓝量:{},战斗力:{},血量:{},闪避：{}'.format(self.name, self.name,self.blue, self.s_atk,self.blood,self.s_avoid))
                else:
                    print('缺少蓝！！！')

     #增加技能
    def add_skill(self,other):
        self.skill.append(other)
        print('{}装备了技能{}'.format(self.name,other.model))


    def add_blood(self):
        self.blood += 100

    #购买装备
    def add_weapon(self,other):
        if self.money >= other.price:
            self.money -= other.price
            self.weapon.append(other.model)
            print('{}购买了武器{}，花费了：{}，金钱剩余：{}'.format(self.name,other.model,other.price,self.money))
            self.use_weapon()
            return True
        else:
            print('{}金钱不足，仅剩：{}'.format(self.name,self.money))
            return False

    #使用装备
    def use_weapon(self):
        for i in range(len(self.skill)):
            self.max_blood += self.skill[i].blood
            self.base_atk +=self.skill[i].atk
            self.base_avoid += self.skill[i].avoid
    #一回合
    def one(self):

        self.s_atk = self.base_atk
        self.s_avoid = self.base_avoid
        if self.blue < self.max_blue:
            self.blue += 1

    def get_hurt(self,ATK):
        if random.random() > self.s_avoid:
            if self.blood <= ATK:
                print('{}被打死了！！！'.format(self.name))
            else:
                self.blood -= ATK
        else:
            print('{}躲避了伤害'.format(self.name))

def main():

    '''
    武器类weapon
        方天画戟：攻击+50---------------100
        霸者重装：blood+200------------80
        红莲斗篷：攻击+20，blood+100----80
        韧性鞋：回避+20%---------------40
        护甲鞋：blood+100-------------40
        宗师之力：被动 * 2-------------100
    '''
    fthj = weapon('方天画戟',0,50,0,0,100,1)
    bzzz = weapon('霸者重装',200,0,0,0,80,1)
    hldp = weapon('红莲斗篷',100,20,0,0,80,1)
    zxx = weapon('韧性鞋',0,0,0.2,0,40,1)
    hjx = weapon('护甲鞋',100,0,0,0,40,1)
    zszl = weapon('宗师之力',0,0,0,0,100,2)

    '''
    skill类 
        被动：
            【战士】浴血奋战----血量越少，战力越高
            【坦克】亢奋-------每回合回少量回血
        主动：
            【战士】奋力一击----blue减2 -----攻击*2     
                    天魔降世----blue减5----（需要购买方天画戟）----攻击*3，回避 = 50%，被动*2
            【坦克】横扫千军----blue减2----攻击*3    
                    凶兽出笼---- blue减5   （blood <= 100） ----攻击*3，回血300   
    '''
    yxfz = skill('浴血奋战',0,0,0,0,'被动',1)
    kf = skill('亢奋',0,0,0,0,'被动',2)
    flyj = skill('奋力一击',0,2,0,2,'主动',1)
    tmjs = skill('天魔降世',0,3,0.5,5,'主动',2)
    hsqj = skill('横扫千军',0,3,0,2,'主动',1)
    xscl = skill('凶兽出笼',300,3,0,5,'主动',1)
    '''
        战士：name  blood=500   ATK(attack)=60 blue= 10 avoid(回避)20%  skill(Q W E)   money = 200
        坦克：name  blood=1000  ATK=40          blue= 6  avoid(回避)10%  skill(Q W E)  money = 200
    '''
    aaa = soldier('战士', '吕布', 500, 60, 0.2, 10)
    bbb = soldier('坦克', '张飞', 1000, 40, 0.1, 8)

    #加载技能
    bbb.add_skill(kf)
    bbb.add_skill(hsqj)
    bbb.add_skill(xscl)
    aaa.add_skill(yxfz)
    aaa.add_skill(flyj)
    aaa.add_skill(tmjs)

    #开始
    print(
            '''
            [1]吕布
            [2]张飞
            '''
    )
    #人物选择
    person = input('人物选择：')
    if person == '1':
        choice(aaa)
        bbb.add_weapon(bzzz)
        bbb.add_weapon(hldp)
        bbb.add_weapon(hjx)
        att(aaa,bbb)
    elif person == '2':
        choice(bbb)
        aaa.add_weapon(fthj)
        aaa.add_weapon(zszl)
        att(bbb,aaa)


#装备选择方法
def choice(hero):
    fthj = weapon('方天画戟', 0, 50, 0, 0, 100, 1)
    bzzz = weapon('霸者重装', 200, 0, 0, 0, 80, 1)
    hldp = weapon('红莲斗篷', 100, 20, 0, 0, 80, 1)
    zxx = weapon('韧性鞋', 0, 0, 0.2, 0, 40, 1)
    hjx = weapon('护甲鞋', 100, 0, 0, 0, 40, 1)
    zszl = weapon('宗师之力', 0, 0, 0, 0, 100, 2)
    while True:
        print(
            '''
            [1]方天画戟：攻击+50---------------100
            [2]霸者重装：blood+200------------80
            [3]红莲斗篷：攻击+20，blood+100----80
            [4]韧性鞋：回避+20%---------------40
            [5]护甲鞋：blood+100-------------40
            [6]宗师之力：被动 * 2-------------100
            [0]退出
            '''
        )
        choice = input('请购买装备：')
        if choice == '1':
            hero.add_weapon(fthj)
        elif choice == '2':
            hero.add_weapon(bzzz)
        elif choice == '3':
            hero.add_weapon(hldp)
        elif choice == '4':
            hero.add_weapon(zxx)
        elif choice == '5':
            hero.add_weapon(hjx)
        elif choice == '6':
            hero.add_weapon(zszl)
        elif choice == '0':
            print('你正在退出装备购买...')
            break
        else:
            print('无法识别,请重新输入')

def att(hero,other):
    i = 0
    while True:
        i += 1
        txt = '王者单机第{}回合'.format(i)
        print(txt.center(100, '*'))
        print(
            '''
            【1】普通攻击
            【2】被动技能：{}
            【3】主动技能：{}
            【4】主动技能：{}
            【0】回血
            '''
        .format(hero.skill[0].model,hero.skill[1].model,hero.skill[2].model))
        choice = input('攻击方式：')
        if choice == '1':
            ATK = hero.attack(other)
            other.get_hurt(ATK)
            ATK2 = other.attack(hero)
            hero.get_hurt(ATK2)
        elif choice == '2':
            hero.use_skill(other,hero.skill[0])
            other.use_skill(hero,other.skill[0])
        elif choice == '3':
            ATK = hero.use_skill(other, hero.skill[1])
            other.get_hurt(ATK)
            ATK2 = other.use_skill(hero, other.skill[1])
            hero.get_hurt(ATK2)
        elif choice == '4':
            ATK =hero.use_skill(other,hero.skill[2])
            other.get_hurt(ATK)
            ATK2 = other.use_skill(hero, other.skill[2])
            hero.get_hurt(ATK2)
        elif choice == '0':
            hero.add_blood()
            ATK2 = other.attack(hero)
            hero.get_hurt(ATK2)
        print('*' * 108)



main()