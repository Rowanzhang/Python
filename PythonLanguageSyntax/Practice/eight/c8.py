def squsum(*param):
    sm = 0
    for i in param:
        sm += i*i
    print(sm)


squsum(1, 3, 4, 5, 6)