a = 1.12386
# 最简单的解决模型
print("Please enter the number of decimal point you want to keep:")
s = int(input())
b = str(a)
print(b[:2+s])
# 还有来做
a = int(a*(10**s)) / (10**s)
print(a)
a = 1.12386
# 循环
# for x in range(0, s):
    # v[0] = int(a)
    # a = v[x+1] = a-v[x]
print(round(a, 3))

