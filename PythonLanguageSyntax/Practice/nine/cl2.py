class Student():
    sun = 0
    name = 'charlie'
    age = 18
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.sun += 1
        print('当前班级学生总数为:'+str(self.__class__.sun))
        print(name)
        print(age)

    def do_homework(self):
        self.__class__.sun += 1
        self.__class__.sun += 1
        print('当前班级学生总数为:'+str(self.__class__.sun))
'''
class Printer():
    def print_file(self,):
        print('name:  ')
        print('age:  '+self.name)
'''


student1 = Student('zhang', 18)
# print(student1.name)
student3 = Student('wang', 23)
# print(Student.name)
# print(student1.__dict__)
# print(Student.__dict__)
# print(id(student1.name))
# print(id(Student.name))
print(student1.do_homework())