Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(i)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    type(i)
NameError: name 'i' is not defined
>>> type(1)
<class 'int'>
>>> type(1.000000000)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> int(Ture)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(Ture)
NameError: name 'Ture' is not defined
>>> int (True)
1
>>> int (False)
0
>>> type(bool(-1))
<class 'bool'>
>>> bool(-1)
True
>>> bool([1,2,3,])
True
>>> bool((1,2,3,))
True
>>> bool(())
False
>>> bool([])
False
>>> bool(None)
False
>>> type("1")
<class 'str'>
>>> type(/r)
SyntaxError: invalid syntax
>>> type(\r)
SyntaxError: unexpected character after line continuation character
>>> type("\r")
<class 'str'>
>>> type([0,])
<class 'list'>
>>> {0,2,1,}
{0, 1, 2}
>>> type({1,2,3})
<class 'set'>
>>> type({key 1 value 2})
SyntaxError: invalid syntax
>>> type(key 1:value 2)
SyntaxError: invalid syntax
