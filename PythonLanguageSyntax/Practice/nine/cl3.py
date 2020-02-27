class Student():
    __sun = 0
    
    def __init__(self, name, age, score):
        self.name = name
        self.__age = age
        self.score = 0 
        self .__do_homework(score)
        print(name)
        print(age)

    def __do_homework(self, score):
        a = 1
        note = "做笔记"
        self.score = score
        self.age = 0
        print(note)

    # def __read_book(self):
    #     print(self.note)
       
    @classmethod
    def __plus_sun(cls):
        cls.__sun += 1
        print()
        print('当前班级学生总数为:'+str(cls.__sun))
    
    @staticmethod
    def __add(x, y):
        print(Student.__sun)
        pass

    def run(self):
        self.__do_homework(self.score)
        # self.__read_book()


student1 = Student('zhang', 18, 45)
# Student.plus_sun()
student3 = Student('wang', 23, 98)
# Student.plus_sun()
# print(student1.do_homework())
# student1.add(1, 2)
# Student.add(2, 1)
student1.run()
s = Student._Student__sun = 1
print(s)
