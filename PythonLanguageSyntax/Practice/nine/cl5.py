from cl4 import Human


class Student(Human):
    def __init__(self, name, age, school):
        super(Student, self).__init__(name, age)


student1 = Student(name='zhang', school='人民路小学', age=18)
print(student1.sun)
print(Student.sun)
# print(student1.name)
# print(student1.age)
student1.get_name()


