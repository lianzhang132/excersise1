"""
a = 10
def fun1():
    a = 100
    def fun2():
        print(a)

fun1()
# print(a)



a =10
def fun1():
    a = 100
    def fun2():
        print(a)
    fun2()
fun1()
print(a)

"""
a = 10

def fun1():
    a = 100
    global a
    def fun2():
        print(a)

    fun2()

fun1()
print(a)