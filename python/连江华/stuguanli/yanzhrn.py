# # for "w" in range(list1):
# stu_li =[   {"name":"张飞","age":"20","sex":"nan"},
#             {"name":"关于","age":"21","sex":"nan"},
#             {"name":"貂蝉","age":"20","sex":"女"},
#             {"name":"小乔","age":"19","sex":"女"},
#
#
#          ]
# # stu_li =[   ("张飞","20","nan"),
# #             ("关于","21","nan"),
# #             ("貂蝉","20","女"),
# #             ("小乔","19","女"),
# #
# #
# #          ]
# sorted(stu_li,key=stu_li[name],reverse = False)
# print(stu_li)
stu_li = [{"sid": "00001", "name": "zhanf", "age": "20", "sex": "nan"}, {"sid": "00002", "name": "lian", "age": "15", "sex": "nan"}, {"sid": "00002", "name": "hua", "age": "18", "sex": "nan\\"}, {"sid": "00003", "name": "hfad", "age": "52", "sex": "kldsa"}, {"sid": "00004", "name": "fha", "age": "jaf", "sex": "fnd"}, {"sid": "00005", "name": ";lian", "age": "dj", "sex": "fddf"}, {"sid": "00006", "name": "djs\\", "age": "gf", "sex": "fjds"}]
# for n in range(0,len(stu_li)):
#     if "zhanf" == stu_li[n]["name"]:
#         print(stu_li[n]["name"])
for n,stu in enumerate(stu_li) :
    list1 = stu.values()
    print(list(list1)[0])
    # for m ,v in enumerate (stu):
    #     print(m)