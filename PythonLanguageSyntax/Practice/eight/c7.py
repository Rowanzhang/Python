print("a", "b", "c")


def deemo(x, m=2, *param):
    print(param)
    print(type(param))


a = (1, 4, 5, 5, 9)
deemo(1, 2,(1, 2, 3, 4))
deemo(1, 2, *a)