Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='        hello        world       "
SyntaxError: unterminated string literal (detected at line 1)
s
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s
NameError: name 's' is not defined
s='        hello       world       '
s
'        hello       world       '
s.strip()
'hello       world'
s.lstrip()
'hello       world       '
s.rstrip()
'        hello       world'
s='strings.py'
s
'strings.py'
s.startswith('str')
True
s.startswith('gfh')
False
s.endswith('py')
True
s.endswith('js')
False
'sdfyui'.isalpha()
True
'DFGHJUYdfghjkuy'.isalpha()
True
'sahith@12345'.isalpha()
False
'2345678'.isalnum()
True
'ewrtyuii'.islower
<built-in method islower of str object at 0x000002453A1DE070>
'sdfgg'.islower()
True
'sdfghjk@123$%^&**'.islower()
True
'ASDFGHJK@#$%^&*(567'.isupper()
True
' '.isspace()
True
'hello          '.issapace()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    'hello          '.issapace()
AttributeError: 'str' object has no attribute 'issapace'. Did you mean: 'isspace'?
'hello     '.isspace()
False
'Py Prg Lan'.istitle()
True
'py_python'.isidentifier()
True
'py@123'.isidentifier()
False
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2,3,4]
m=[7,5,4,3]
l+m
[1, 2, 3, 4, 7, 5, 4, 3]
l*4
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l=[10,20,30,40,50]
l[4]
50
l[3]
40
l[2]
30
l[1]
20
l[0]
10
l[-1]
50
l[-2]
40
l[-3]
30
l[-4]
20
l[-5]
10
l[::1]
[10, 20, 30, 40, 50]
l[:2:1]
[10, 20]
l[:3:1]
[10, 20, 30]
l[:4:1]
[10, 20, 30, 40]
l[:5:1]
[10, 20, 30, 40, 50]
l[::-1]
[50, 40, 30, 20, 10]
l[-1:-4:-1]
[50, 40, 30]
l[-3::-1]
[30, 20, 10]
20 in l
True
30 in l
True
70 not in l
True
80 in l
False
l[1]=70
l
[10, 70, 30, 40, 50]
id(1)
140734371251320
l
[10, 70, 30, 40, 50]
l.append(120)
l
[10, 70, 30, 40, 50, 120]
l.append(400)
l
[10, 70, 30, 40, 50, 120, 400]
l.insert(20)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    l.insert(20)
TypeError: insert expected 2 arguments, got 1
l.insert(4,50)
l
[10, 70, 30, 40, 50, 50, 120, 400]
l.extend([80,90,110])
l
[10, 70, 30, 40, 50, 50, 120, 400, 80, 90, 110]
l.pop()
110

l
[10, 70, 30, 40, 50, 50, 120, 400, 80, 90]
l.pop()(
l
exit90
SyntaxError: '(' was never closed
l.pop()
90
l
[10, 70, 30, 40, 50, 50, 120, 400, 80]
l.pop()
80
l
[10, 70, 30, 40, 50, 50, 120, 400]
l.pop(3)
40
l
[10, 70, 30, 50, 50, 120, 400]
>>> l.remove(400)
>>> l
[10, 70, 30, 50, 50, 120]
>>> l.remove(50)
>>> l
[10, 70, 30, 50, 120]
>>> del l[4]
>>> l
[10, 70, 30, 50]
>>> del l[2]
>>> l
[10, 70, 50]
>>> del l[1]
>>> l
[10, 50]
>>> l.clear()
>>> l
[]
>>> id[l]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    id[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> id(l)
2496308020416
>>> l=[200,30,33,42,10,70,50,40,100,120,400]
>>> sorted(1)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    sorted(1)
TypeError: 'int' object is not iterable
>>> sorted(l)
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
>>> l.sort()
>>> l
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
>>> min(l)
10
>>> max(l)
400
>>> l.reverse()
>>> l
[400, 200, 120, 100, 70, 50, 42, 40, 33, 30, 10]
>>> sorted(l,reverse=True)
[400, 200, 120, 100, 70, 50, 42, 40, 33, 30, 10]
>>> l.sort(1,2)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    l.sort(1,2)
TypeError: sort() takes no positional arguments
>>> l.index(50)
5
>>> l.index(50)
5
>>> l.index(120)
2
>>> l.index(99)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    l.index(99)
ValueError: list.index(x): x not in list
>>> l.count(30)
1
>>> l.count(120)
1
>>> l.count(99)
0
