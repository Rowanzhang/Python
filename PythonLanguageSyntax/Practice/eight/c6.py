def print_student_file(name, gender="男", age=18, college="人民路小学"):
    print("我叫" + name)
    print("我今年" + str(age) + "岁")
    print("我是" + gender + "生")
    print("我在" + college + "上学")


print_student_file("鸡小萌", "man", 18, "人民路小学")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print_student_file("石敢当", "女", )
print_student_file(age=17, "果果", gender="女", college="光名小学")