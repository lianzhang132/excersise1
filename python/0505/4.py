class Man:
    # def __new__(cls, *args, **kwargs):
    #     color = "red"

    def __init__(self):
        color = "green"
    def getco(self):
        print(self.color)

dema = Man()
lisa = Man()
huangzi = Man()
print(id(dema))
print(id(lisa))
print(id(huangzi))
print(id(Man))

