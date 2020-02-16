Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type({1:1})
<class 'dict'>
>>> 基本的数据类型
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    基本的数据类型
NameError: name '基本的数据类型' is not defined
>>> 可变与不可变
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    可变与不可变
NameError: name '可变与不可变' is not defined
>>> (1,2,3)[2]==2
False
>>> (1,2,3)[2]=2
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    (1,2,3)[2]=2
TypeError: 'tuple' object does not support item assignment
>>> a=878
>>> a
878
>>> b=dsjkdakh
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b=dsjkdakh
NameError: name 'dsjkdakh' is not defined
>>> b="dashdaj"
>>> b
'dashdaj'
>>> a=12
>>> b=a
>>> b=67
>>> a=12
>>> b=a
>>> a=67
>>> b
12
>>> a=12
>>> id(a)
140728003315712
>>> b=a
>>> id(b)
140728003315712
>>> a=78
>>> id(a)
140728003317824
>>> id(b)
140728003315712
>>> a=(0,1,2,3)
>>> id(a)
2095377313440
>>> a=(0,1,2,3,4)
>>> id(a)
2095377311280
>>> a=[1,2,3]
>>> a.append(5)
>>> a
[1, 2, 3, 5]
>>> a=(0,1,2)[2]=8
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a=(0,1,2)[2]=8
TypeError: 'tuple' object does not support item assignment
>>> a.append(3)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.append(3)
AttributeError: 'int' object has no attribute 'append'
>>> 1+2
3
>>> 1-2
-1
>>> 1*1
1
>>> 1**2
1
>>> 2**2
4
>>> 1/1
1.0
>>> 1//1
1
>>> 1%2
1
>>> 2%1
0
>>> 1=2
SyntaxError: cannot assign to literal
>>> a=2
>>> a+=2
>>> a
4
>>> a=a+2
>>> a
6
>>> "sdjahd">"sdjahdjka"
False
>>> (1,2,4,5)<=(121,2,5,4)
True
>>> 1,2,4,5)>=(121,2,5,4)
SyntaxError: unmatched ')'
>>> (1,2,4,5)<=(121,2,5,4)
True
>>>  (1,2,4,5)>=(121,2,5,4)
 
SyntaxError: unexpected indent
>>> (1,2,4,5)<=(121,2,5,4)
True
>>> (1,2,4,5)>=(121,2,5,4)
False
>>>  "asajd" and ""
 
SyntaxError: unexpected indent
>>> "asd" and ""
''
>>> "" and "sdjha"
''
>>> "a" and "b"
'b'
>>> 0  and ""
0
>>> 0 or ""
''
>>> 1 or 2
1
>>> 1 or 0
1
>>> 0 or 1
1
>>> a =2
>>> a in (0,1,2,3)
True
>>> a={1,2,3,4,5}
>>> b={2,1,4,3,6}
>>> a==b
False
>>> b={2,1,4,3,5}
>>> a==b
True
>>> a=(1,2,3,4)
>>> b=(2.1.4.3)
SyntaxError: invalid syntax
>>> b=(2.1.4.3)
SyntaxError: invalid syntax
>>> b=(2,1,4,3)
>>> a==b
False
>>> a is b
False
>>> a not is b
SyntaxError: invalid syntax
>>> identify --hlep
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    identify --hlep
NameError: name 'identify' is not defined
>>> identify --help
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    identify --help
NameError: name 'identify' is not defined
>>> is --help
SyntaxError: invalid syntax
>>> is -help
SyntaxError: invalid syntax
>>> not in
SyntaxError: invalid syntax
>>> in
SyntaxError: invalid syntax
>>>  23 & 23
 
SyntaxError: unexpected indent
>>> 23 & 12
4
>>> &
SyntaxError: invalid syntax
>>> |
SyntaxError: invalid syntax
>>> 23|12
31
>>> bin(23)
'0b10111'
>>> bin(12)
'0b1100'
4
>>> 表达式：运算符+操作数组成的一个序列组
SyntaxError: invalid character in identifier
>>> 