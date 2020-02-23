class Student():
    name = 'charlie'
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def do_homework():
        print('do my homework')

'''
class Printer():
    def print_file(self,):
        print('name:  ')
        print('age:  '+self.name)
'''


student1 = Student('zhang', 18)
print(student1.name)
student3 = Student('wang', 23)
print(Student.name)
