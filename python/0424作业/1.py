import json
file = open("wenjian","r+")

list1 = ["hha","hehhe","heiheieh","henge"]
# json.dump(list1,file)
# # json.dump("datetime",file)
print(json.load(file))
# print(json.loads(json.dumps(list1)))