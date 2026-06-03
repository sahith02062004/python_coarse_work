Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="python programming"
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord('a')
97
ord('A')
65
char('a')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    char('a')
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(98)
'b'
chr(120)
'x'
chr(30)
'\x1e'
chr(35)
'#'
chr(37)
'%'
chr(50)
'2'
chr(500)
'Ǵ'
chr(50000)
'썐'
chr(32)
' '
chr(65)
'A'
s='python Programming'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON pROGRAMMING'
s.casefold()
'python programming'
s.center(38,*)
SyntaxError: Invalid star expression
s.center(38,'*')
'**********python Programming**********'
s.1just(28,'-')
SyntaxError: invalid imaginary literal
s.rjust(28,'-')
'----------python Programming'
'123'.zfill(5)
'00123'
'123'.zfill(10)
'0000000123'
'123'.zfill(3)
'123'
'123'.zfill(2)
'123'
s.find('g')
10
s.rfind('z')
-1
s.omdex('o')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s.omdex('o')
AttributeError: 'str' object has no attribute 'omdex'. Did you mean: 'index'?
s.rindex('o')
9
s.index('z')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s.count('y')
1
s.count('m')
2
s.count('g')
2
s
'python Programming'
s.replace('python','java')
'java Programming'
s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('python','123456')



            exit
            
SyntaxError: '(' was never closed
s.translate(s.maketrans('python','123456'))
            
'123456 Pr5grammi6g'
s='java,python,javascript,c,c++'
            
s.split(',')
            
['java', 'python', 'javascript', 'c', 'c++']
s.split(',',2)
            
['java', 'python', 'javascript,c,c++']
s.rsplit(',',2)
            
['java,python,javascript', 'c', 'c++']
g='sdfgh'
            
s.split(':')
            
['java,python,javascript,c,c++']
s.split(';')
            
['java,python,javascript,c,c++']
s.split('.')
            
['java,python,javascript,c,c++']
s.split(',,,')
            
['java,python,javascript,c,c++']
>>> g='sdfgh'
...             
>>> g='''dsfghjk'''
...             
>>> g='''dfghjk
... fghjkl;
... gfhjkl
... drtyuhj'''
...             
>>> g
...             
'dfghjk\nfghjkl;\ngfhjkl\ndrtyuhj'
>>> s.splitlines()
...             
['java,python,javascript,c,c++']
>>> g.splitlines()
...             
['dfghjk', 'fghjkl;', 'gfhjkl', 'drtyuhj']
>>> l=['java', 'python', 'javascript', 'c', 'c++']
...             
>>> ''.join(1)
...             
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
>>> ''.join(1)
...             
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
>>> l=['java', 'python', 'javascript', 'c', 'c++']
...             
>>> ''.join(l)
...             
'javapythonjavascriptcc++'
>>> '@'.join(1)
...             
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    '@'.join(1)
TypeError: can only join an iterable
>>> '@'.join(l)
...             
'java@python@javascript@c@c++'
>>> ''.join(l)
...             
'javapythonjavascriptcc++'
>>> ','.join(l)
...             
'java,python,javascript,c,c++'
>>> s
...             
'java,python,javascript,c,c++'
>>> s.partitiom(',')
...             
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    s.partitiom(',')
AttributeError: 'str' object has no attribute 'partitiom'. Did you mean: 'partition'?
>>> s.partition(',')
...             
('java', ',', 'python,javascript,c,c++')
>>> s.rpartition(',')
...             
('java,python,javascript,c', ',', 'c++')
