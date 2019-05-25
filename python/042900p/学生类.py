import json

class student():

    id = 1
    name ="小明"
    grade = "san"
    room = "python"

    @staticmethod
    def coun():
        student.id+=1
        print("我是第"+str(student.id)+"个学生")

stu1 = student
stu1.name = "小红"
stu1.coun()
print(student.name)
stu1.name = "小江"
stu1.coun()
print(student.name)
stu1.name = "小李"
stu1.coun()
print(student.name)
