Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d[1]='int
SyntaxError: unterminated string literal (detected at line 1)
d={}
d=dicg()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    d=dicg()
NameError: name 'dicg' is not defined. Did you mean: 'dict'?
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]=
SyntaxError: invalid syntax
d[1]='int'
d
{1: 'int'}
d[1.2]="float"
d
{1: 'int', 1.2: 'float'}
type(d)
<class 'dict'>
d[5+6j]='complex'
d
{1: 'int', 1.2: 'float', (5+6j): 'complex'}
d['demo']='str'
d
{1: 'int', 1.2: 'float', (5+6j): 'complex', 'demo': 'str'}
d[[1,2,3,4,5]]='list'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[[1,2,3,4,5]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[(1,2,3,4,5)]='tuple'
d
{1: 'int', 1.2: 'float', (5+6j): 'complex', 'demo': 'str', (1, 2, 3, 4, 5): 'tuple'}
d[{1,2,3)]='set'
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
d[[1:2,2:3]]='dict'
SyntaxError: invalid syntax
d[False]='bool'
d
{1: 'int', 1.2: 'float', (5+6j): 'complex', 'demo': 'str', (1, 2, 3, 4, 5): 'tuple', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d[2]='sdghgh'
d[4]=3+1j
d[5]=[1,2,3]
d[6]=(1,2,3,4)
d{7)={1,2)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
d[7]=(1,2)
d[8]={1:2,2:2}
d(9)=False
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
d
{1: 1, 23: 23.4, 2: 'sdghgh', 4: (3+1j), 5: [1, 2, 3], 6: (1, 2, 3, 4), 7: (1, 2), 8: {1: 2, 2: 2}}
d[9]=False
d
{1: 1, 23: 23.4, 2: 'sdghgh', 4: (3+1j), 5: [1, 2, 3], 6: (1, 2, 3, 4), 7: (1, 2), 8: {1: 2, 2: 2}, 9: False}
d[1]=12
d
{1: 12, 23: 23.4, 2: 'sdghgh', 4: (3+1j), 5: [1, 2, 3], 6: (1, 2, 3, 4), 7: (1, 2), 8: {1: 2, 2: 2}, 9: False}
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[4]
8
d[6]
12
d[1]
2
d[4]
8
d{'ajay':89, 'harish':76, 'subbu':90, 'nagendra':60,'dinesh':50}
SyntaxError: invalid syntax
d={'ajay':89, 'harish':76, 'subbu':90, 'nagendra':60,'dinesh':50}
a[ajay]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a[ajay]
NameError: name 'a' is not defined
d[ajay]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d[ajay]
NameError: name 'ajay' is not defined
d=ajay
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    d=ajay
NameError: name 'ajay' is not defined
d['harish']
76
d.get('sahith')
d['sahith']
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d['sahith']
KeyError: 'sahith'
d.get['sahith']
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    d.get['sahith']
TypeError: 'builtin_function_or_method' object is not subscriptable
d.get['sahith']
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    d.get['sahith']
TypeError: 'builtin_function_or_method' object is not subscriptable
d.clear('ajay')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d.clear('ajay')
TypeError: dict.clear() takes no arguments (1 given)
d.get('ajay')
89
d.get('subbu','user not found')
90
d.get('sahith','user not found')
'user not found'
d
{'ajay': 89, 'harish': 76, 'subbu': 90, 'nagendra': 60, 'dinesh': 50}
'harish' in d
True
'sahith' not in d
True
d.keys()
dict_keys(['ajay', 'harish', 'subbu', 'nagendra', 'dinesh'])
d.values()
dict_values([89, 76, 90, 60, 50])
d.items()
dict_items([('ajay', 89), ('harish', 76), ('subbu', 90), ('nagendra', 60), ('dinesh', 50)])
>>> sorted(d)
['ajay', 'dinesh', 'harish', 'nagendra', 'subbu']
>>> max(d)
'subbu'
>>> min(d)
'ajay'
>>> len(d)
5
>>> d
{'ajay': 89, 'harish': 76, 'subbu': 90, 'nagendra': 60, 'dinesh': 50}
>>> d['ajay']=100
>>> 
>>> d
{'ajay': 100, 'harish': 76, 'subbu': 90, 'nagendra': 60, 'dinesh': 50}
>>> d['harish']=90
>>> d
{'ajay': 100, 'harish': 90, 'subbu': 90, 'nagendra': 60, 'dinesh': 50}
>>> d.update({'praneeth':90,'manideep':80})
>>> d
{'ajay': 100, 'harish': 90, 'subbu': 90, 'nagendra': 60, 'dinesh': 50, 'praneeth': 90, 'manideep': 80}
>>> d.popitem()
('manideep', 80)
>>> d
{'ajay': 100, 'harish': 90, 'subbu': 90, 'nagendra': 60, 'dinesh': 50, 'praneeth': 90}
>>> d.popitem()
('praneeth', 90)
>>> d
{'ajay': 100, 'harish': 90, 'subbu': 90, 'nagendra': 60, 'dinesh': 50}
>>> d.pop('ajay')
100
>>> d
{'harish': 90, 'subbu': 90, 'nagendra': 60, 'dinesh': 50}
>>> del d[1]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    del d[1]
KeyError: 1
>>> del d('harish')
SyntaxError: cannot delete function call
>>> del d[]
SyntaxError: invalid syntax
>>> d
{'harish': 90, 'subbu': 90, 'nagendra': 60, 'dinesh': 50}
>>> del d['subbu']
>>> d
{'harish': 90, 'nagendra': 60, 'dinesh': 50}
>>> d.clear()
>>> d
{}
>>> d.setdefault('rishi')
>>> d.setdefault('rishi',0)
>>> d
{'rishi': None}
>>> d=
KeyboardInterrupt
>>> d={'ajay': 89, 'harish': 76, 'subbu': 90, 'nagendra': 60, 'dinesh': 50}
>>> d
{'ajay': 89, 'harish': 76, 'subbu': 90, 'nagendra': 60, 'dinesh': 50}
>>> d.setdefault('rishi',0)
0
>>> d.setdefault('satish',0)
0
>>> d.setdefault('harish',0)
76
>>> d
{'ajay': 89, 'harish': 76, 'subbu': 90, 'nagendra': 60, 'dinesh': 50, 'rishi': 0, 'satish': 0}
