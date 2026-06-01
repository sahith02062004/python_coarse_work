Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input()
sahith
name
'sahith'
name=input("enter your name:")
enter your name:harish
name
'harish'
age = input("enter your age:")
enter your age:21
age
'21'
age=int(input("enter your age:"))
enter your age:21
age
21
type(age)
<class 'int'>
gpa=float(input("enter the cgpa:"))
enter the cgpa:6.9
type(gpa)
<class 'float'>
names=input("enter names:").split()
enter names:subbu nag hari sahith rishi vamsi
names
['subbu', 'nag', 'hari', 'sahith', 'rishi', 'vamsi']
products=input("enter product:").split()
enter product:laptop mouse charger keyboard
products
['laptop', 'mouse', 'charger', 'keyboard']
topics=tuple(input("enter topics:").split())
enter topics:token statement variable comment
topics
('token', 'statement', 'variable', 'comment')
op=set(input("enter operators:").split())
enter operators:in not in is not and or not
op
{'is', 'or', 'in', 'and', 'not'}
a=map(int,input().split())
12 34 64 23 1
a
<map object at 0x000001FCC32B6140>
b=list(map(int,input("enter marks:").split()))
enter marks:1 3 4 56 345
b
[1, 3, 4, 56, 345]
prices=tuple(map(int,input("enter prices:").split()))
enter prices:123 345 67 23
prices
(123, 345, 67, 23)
rating=set(map(float,input("enter rating:").split()))
enter rating:12.3 23.5 34.5 6.7
rating
{34.5, 12.3, 6.7, 23.5}
per = list(map(float,input("enter the percentage:").split()))
enter the percentage:5.3 23.5 45.7 12.7
per
[5.3, 23.5, 45.7, 12.7]
prices=tuple(map(float,input("enter the prices:")))
enter the prices:332 345 567 345
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    prices=tuple(map(float,input("enter the prices:")))
ValueError: could not convert string to float: ' '
prices=set(map(float,input("enter the prices:").split()))
enter the prices:234 345 678 89
prices
{89.0, 345.0, 234.0, 678.0}
username,password=input().split()
sahith s@123
username
'sahith'
password
's@123'
a,b,c,d=list(map(int,input("enter 4 values").split()))
enter 4 values2 4 6 8
a
2
b
4
c
6
d
8
price,discount=list(map(float,input("enter the price and discount:").split()))
enter the price and discount:345667 89.2
price
345667.0
discount
89.2
a=eval(input())
356
a
356
a=eval(input())
123.456
a
123.456
a=eval(input())
sahith
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'sahith' is not defined
a

a=eval(input())
sahith
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'sahith' is not defined
a=eval(input())

"string"
a
'string'
a=eval(input())
[1,2,3,4,5]
a
[1, 2, 3, 4, 5]
a=eval(input())
(1,2,3,4,5)
a
(1, 2, 3, 4, 5)
a=eval(input)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a=eval(input)
TypeError: eval() arg 1 must be a string, bytes or code object
a=eval(input())
{1,2,3,4,5}
a
{1, 2, 3, 4, 5}
a=eval(input())
{1:2,3:4,5:6}
a
{1: 2, 3: 4, 5: 6}
a=eval(input())
{d:1,b:2,c:3}

a
{8: 1, 4: 2, 6: 3}
>>> a=eval(input())
true
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a=eval(input())
true
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a=eval(input())
... 
True
>>> a
True
>>> type(a)
<class 'bool'>
>>> a='sahith'
>>> b='sriramoju'
>>> a+b
'sahithsriramoju'
>>> #repetition
>>> a*10
'sahithsahithsahithsahithsahithsahithsahithsahithsahithsahith'
>>> '*'*5
'*****'
>>> #indexing
>>> names='harish sahith'
>>> names[0]
'h'
>>> names[-1]
'h'
>>> names[:5]
'haris'
>>> names[2:7]
'rish '
>>> names[-9::-1]
'sirah'
>>> #slicing
>>> harish sahith rohith'
SyntaxError: unterminated string literal (detected at line 1)
>>> names[5:]
'h sahith'
>>> #membership
>>> s=[a,b,c,d,e,f]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s=[a,b,c,d,e,f]
NameError: name 'e' is not defined
>>> s='hello world'
>>> 'a' in s
False
>>> 'e' in s
True
>>> t=[1,2,3,4]
>>> 2 in t
True
>>> 5 in t
False
>>> 3 not in t
False
