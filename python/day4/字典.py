dic1 = {"date":"monsday","adds":"yunhe","teacher":"zhao","stud":"dic"}
print(dic1)
dic2 =dict(date="monsday",adds = "yunhe",teacher = "zhao",stud ="dic")
print(dic2)

# print(len(dic1))
# print(len(dic2))
# print(max(dic1))
# print(min(dic1))
# print(max(dic2))
# print(min(dic2))
#
# print(dic1["date"])
# print(dic1.get("adds1","none"))
# print(dic2.setdefault("adds1","又没有哦"))
# print(dic2)
dic1["date"]="tuesday"

print(dic1)
dic1["language"]="chinese"
print(dic1)
del dic1["language"]
print(dic1)
print(dic1.pop("date"))
# dic1.clear()
# print(dic1)
# del dic1
# print(dic1)
dic1.update(dic2)
print(dic1)
print(list(dic2.items()))
print(list(dic2.keys()))
print(list(dic2.values()))
