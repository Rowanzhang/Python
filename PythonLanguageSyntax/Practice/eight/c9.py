def city_temp(**param):
    for key, value in param.items():
        print(key, ":", value)
    print(param.items())
    pass


city_temp(bj="32c", xm="23c")