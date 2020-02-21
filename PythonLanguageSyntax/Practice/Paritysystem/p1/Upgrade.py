import random    


def stone4p():
    if random.randrange(0, 100, 1) < 48:
        return True
    else:
        return False


def stone4g():
    fail = success = sumcount = 0
    while True:
        print("你想要升级4级风行石吗？")
        if stone4p():
            print("你获得了一块4级风行石")
            success += 1
        else:
            print("升级失败，将返回你的体力值")
            fail += 1
        if success >= 12:
            sumcount = success + fail
            break
    print("你已经获得了"+str(success)+"块4级风行石")
    return sumcount, fail



def stone6g(sumcount, fail):
    print("你想升级一块6级风行石吗？")
    gold = 29.297*sumcount - fail*10.0 + 19.75 + 10.0
    print("你获得了一块6级")
    return gold





