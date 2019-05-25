def ac():
    a = 5
    def  b():
        print(a)
    return b

ac1 = ac()
ac1()