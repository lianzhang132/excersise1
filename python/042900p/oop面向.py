class computer():
    brand = "弘基"
    display = "noc"
    __minboard= "inter"
    def __init__(self,brand = "大奖"):
        self.brand = brand
    @staticmethod
    def can(serchmovie):
        print(cp.brand+"playing game"+serchmovie)
    def __del__(self):
        print("这是一个%s显示器"%self.display)

cp = computer()
# cp.brand = "lennoer"
print(cp.brand)
# cp.can("看电影")