def a():
    print("a")
def b():
    print("b")
meth = input("请输入方法名：").strip()
import sys
module = sys.modules[__name__]
if hasattr(module,meth):
    getattr(module,"b")
else:
    print("输入不对")