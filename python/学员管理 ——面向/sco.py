from prettytable import PrettyTable
import json
import os
import stu

file1 = open("info", "r")
stu_info_li = json.load(file1)

class Score:
    def sub_add(self):
        for n, stu in enumerate(stu_info_li):

