Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,1.1.'trly',[])
SyntaxError: invalid syntax
t
(1, 1, 1, 1, 1)
t=(1,1.1,'truly',[])
t
(1, 1.1, 'truly', [])
h=(10,20,30,40,50)
t=(90,80,70)
t+h
(90, 80, 70, 10, 20, 30, 40, 50)
t*4
(90, 80, 70, 90, 80, 70, 90, 80, 70, 90, 80, 70)
h
(10, 20, 30, 40, 50)
h[1]
20
h[2]
30
h[3]
40
h[4]
50
h[-1]
50
h[-2]
40
h[-3]
30
h[-4]
20
h[5]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    h[5]
IndexError: tuple index out of range
h[-5]
10
h[::]
(10, 20, 30, 40, 50)
h[1::]
(20, 30, 40, 50)
h=[2::]
SyntaxError: invalid syntax
h=[2::]
SyntaxError: invalid syntax
h[:3]
(10, 20, 30)
t
(90, 80, 70)
h[3:]
(40, 50)
h[1:4]
(20, 30, 40)
h[2:]
(30, 40, 50)
h[::2]
(10, 30, 50)
h[::3]
(10, 40)
h[::4]
(10, 50)
h[::5]
(10,)
h[::-1]
(50, 40, 30, 20, 10)
h[::-2]
(50, 30, 10)
h[::-3]
(50, 20)
h[::-4]
(50, 10)
h[::-5]
(50,)
h[::-6]
(50,)
h[-1:-4]
()
h[-1:-4:-1]
(50, 40, 30)
h
(10, 20, 30, 40, 50)
10 in h
True
30 in h
True
60 in t
False
60 not in h
True
10 not in h
False
len(h)
5
sorted(h)
[10, 20, 30, 40, 50]
sort(h)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sort(h)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
min(h)
10
max(h)
50
sum(t)
240
t.count(10)
0
h.count(10)
1
t.index(10)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    t.index(10)
ValueError: tuple.index(x): x not in tuple
h.index(10)
0
a,b,c=1,2,3
a
1
b
2
c
3
a=(1,2,4)
a
(1, 2, 4)
x,y,z=a
x
1
y
2
z
4
t=(1,2,3,[4,5,6],7,,8
   
SyntaxError: invalid syntax
t=(1,2,3,[4,5,6],7,8)
   
t
   
(1, 2, 3, [4, 5, 6], 7, 8)
t[2]
   
3
t[4]
   
7
t[3]
   
[4, 5, 6]
t[2]=4
   
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
t[3]
   
[4, 5, 6]
t[3].append(10)
   
t
   
(1, 2, 3, [4, 5, 6, 10], 7, 8)
s={1,2,3,4}
   
s=set()
   
s
   
set()
s={1,1,1,1,1}
   
s
   
{1}
s={987,654,345,56,345,1,2,34,6,56}
   
s
   
{1, 2, 34, 6, 654, 56, 345, 987}
s=set()
   
s
   
set()
s.add(1)
   
s
   
{1}
s.add(3.89)
   
s
   
{1, 3.89}
s.add(56.567)
   
s
   
{56.567, 1, 3.89}
s.add("kjhy")
   
s
   
{56.567, 1, 3.89, 'kjhy'}
a.ass([1,2,3,4,4])
   
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a.ass([1,2,3,4,4])
AttributeError: 'tuple' object has no attribute 'ass'
s.entend([1,2,3])
   
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    s.entend([1,2,3])
AttributeError: 'set' object has no attribute 'entend'
s.count(1,2,3)
   
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    s.count(1,2,3)
AttributeError: 'set' object has no attribute 'count'
s
   
{56.567, 1, 3.89, 'kjhy'}
s.add({1,2,3,4})
   
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add({1:2,2:3})
   
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    s.add({1:2,2:3})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add(false)
   
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    s.add(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
s=
   
SyntaxError: invalid syntax
s
   
{56.567, 1, 3.89, 'kjhy'}
s.add((1,2,3,4))
   
s
   
{1, 3.89, (1, 2, 3, 4), 'kjhy', 56.567}

s.add(false)
   
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    s.add(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
1 in s
   
True
2 in s
   
False
false in s
   
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    false in s
NameError: name 'false' is not defined. Did you mean: 'False'?
false not in s
   
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    false not in s
NameError: name 'false' is not defined. Did you mean: 'False'?
s.add(False)
   
s
   
{False, 1, 3.89, (1, 2, 3, 4), 'kjhy', 56.567}
False in s
   
True
False not in s
   
False
a={1,2,3,5,6,8,10}
   
b={6,7,8,9}
   
a.union(b)
   
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.intersection(b)
   
{8, 6}
a & b
   
{8, 6}
a.proportion(b)
   
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    a.proportion(b)
AttributeError: 'set' object has no attribute 'proportion'
a | b
   
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a-b
   
{1, 2, 3, 5, 10}
a^b
   
{1, 2, 3, 5, 7, 9, 10}
a
   
{1, 2, 3, 5, 6, 8, 10}
a<={1}
   
False
a>={1}
   
True
a>={1,3}
   
True
a<={6,8}
   
False
a<={6}
   
False
a<={8}
   
False
a<={1,2,3,4,5,6,8,10,11,12}
   
True
a>={6,10,8}
   
True
a
   
{1, 2, 3, 5, 6, 8, 10}
b
   
{8, 9, 6, 7}
a.isdisjoint(b)
   
False
>>> a.isdisjoint({90,80})
...    
True
>>> a.add(90)
...    
>>> a
...    
{1, 2, 3, 5, 6, 90, 8, 10}
>>> a.add(17)
...    
>>> a
...    
{1, 2, 3, 5, 6, 8, 10, 17, 90}
>>> a.update(11,12,13)
...    
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    a.update(11,12,13)
TypeError: 'int' object is not iterable
>>> a.update({11,12,13})
...    
>>> a
...    
{1, 2, 3, 5, 6, 8, 10, 11, 12, 13, 17, 90}
>>> a.pop()
...    
1
>>> a.pop()
...    
2
>>> a.remove(6)
...    
>>> a
...    
{3, 5, 8, 10, 11, 12, 13, 17, 90}
>>> a.remove(6)
...    
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    a.remove(6)
KeyError: 6
>>> a.discard(6)
...    
>>> a
...    
{3, 5, 8, 10, 11, 12, 13, 17, 90}
>>> a.discard(8)
...    
>>> a
...    
{3, 5, 10, 11, 12, 13, 17, 90}
>>> a.discard(8)
...    
>>> a
...    
{3, 5, 10, 11, 12, 13, 17, 90}
>>> a.remove(8)
...    
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    a.remove(8)
KeyError: 8
>>> a.discard(8)
...    
>>> a
...    
{3, 5, 10, 11, 12, 13, 17, 90}
