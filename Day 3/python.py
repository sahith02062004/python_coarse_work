Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=1+i4
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=1+i4
NameError: name 'i4' is not defined. Did you mean: 'id'?
a=1+ib
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a=1+ib
NameError: name 'ib' is not defined. Did you mean: 'id'?
a=2

clear()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
clear
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
s='pyhton'
id(s)
2461017873728
s="java"
id(s)
2463128285232
a=[1,2,3,4,5]
id(a)
2461018019328
a.append(10)
a.append(20)
a
[1, 2, 3, 4, 5, 10, 20]
a
[1, 2, 3, 4, 5, 10, 20]
a=[1,2,2]
a
[1, 2, 2]
1=[]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1=[]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[]
type(1)
<class 'int'>
l=[]
1=list()
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
type(1)
<class 'int'>
1=[]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[]
l=list()
type(1)
<class 'int'>
s=[a,b,c,d]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s=[a,b,c,d]
NameError: name 'b' is not defined
a=["apples","mangoes","jam"]
a=["apples","mangoes","jam"]
type(a)
<class 'list'>
<class 'list'>
SyntaxError: invalid syntax
>>> a=none
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> a=
SyntaxError: invalid syntax
>>> a=10
>>> type(a)
<class 'int'>
>>> b=8.0
>>> type(b)
<class 'float'>
>>> c=1+j
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    c=1+j
NameError: name 'j' is not defined
>>> c=1+2j
>>> type(c)
<class 'complex'>
>>> s='pyhton'
>>> type(s)
<class 'str'>
>>> s='python'
>>> id(s)
2463120342688
>>> s='pyhton'
>>> s='java'
>>> print(s)
java
>>> s"pyhton"
SyntaxError: invalid syntax
>>> s='python"
SyntaxError: unterminated string literal (detected at line 1)
>>> s="python"
>>> id(s)
2463120342688
>>> s="java"
>>> id(s)
2463128285232
>>> 1=['post1.png','reel1.png']
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> s=set()
>>> s={45678,546,3456,13423}
>>> a
10
>>> s
{3456, 546, 45678, 13423}
>>> b
8.0
>>> u
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    u
NameError: name 'u' is not defined
>>> a
10
>>> s={1,1,1,2}
>>> s
{1, 2}
>>> dist={'name=sahith','course=pfs'}
>>> type(dist)
<class 'set'>
>>> d=("name=sahith","age=100"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> d={"name=sahith"}
