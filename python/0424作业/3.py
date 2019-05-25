import shelve
shle = shelve.open("wejgfgt")
# shelve["name"]="dama"
list1 = ["zhangfei","guayu","liubei"]
shle["name"]= list1
# del shle["name"]
shle["name"] = "lisa"
print(shle["name"])
print(shle.get("name"))
print(shle.setdefault("sex"))