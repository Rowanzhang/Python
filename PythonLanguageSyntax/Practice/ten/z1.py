import re


a = 'C|C++|java|C#|Python|Javascript'

r = re.findall('PHP', a)
if len(r) > 0:
    print('字符串中包含PHP')
else:
    print('No')
