'''for var in seq:
    print(var)
s="python programming"
for ch in s:
    print(ch)
l= ['sugar','salt','oil','eggs']
for item in l:
    print(item)
t= ('1.intro','2.Tokens','3.Data types')
for  i in t:
    print(i)
s={'laptop','mouse','keyboard','phone','charger'}
for i in s:
    print(i)
s={'name':'sahith','batch':'PFS','skills':['python','java',]}
for i in s:
   print(i)
#range(start,stop+1,step) => (0,n,1)
for i in range (1,11):
    print(i)
for i in range(2,51,2):
    print(i)
for i in range(5,101,5):
    print(i)
for i in range(20,0,-1):
    print(i)
for i in range(30,2,-3):
    print(i)
for i in range(6):
    print(i)
for i in range(1,50,2):
    print(i)
for i in range(1,50,3):
    print(i)
a=int(input())
b=int(input())
c=a*b
for c in range(1,100):
    print(c)
s= 'looping statements'
for i in range(len(s)):
    print(i,s[i])
l= [7,2,4,8,3,1,5]
for i in range(len(l)):
    print(i,l[i])
l =(7,2,4,8,3,1,5)
for i in range(len(l)):
    print(i,l[i])
s='looping'
for i in enumerate(s):
    print(i[0],i[1])
l =[7,2,354,56,6]
for i in enumerate(l):
    print(i[0],i[1])
t=(7,6,5,4,3)
for i in enumerate(t):
    print(i[0],i[1])
k={3,5,5,6,7,9}
for i in enumerate(k):
    print(i[0],i[1])
for i in range(10):
    pass
for i in range(10):
    if i==5:
        break
    print(i)
    
for i in range(10):
    if i==5:
        continue
    print(i)
s= 'looping statements'
for i in s:
    if i in "a,e,i,o,u":
        print(i)
l=[56,34,5,6,8,23,56,335,4,9]
for i in l:
    if i%2==0:
        print(i)
l=[56,34,5,6,8,23,56,335,4,9]
for i in l:
    if i%2!=0:
        print(i)
d={'laptop':0,'charger':2,'keyboard':10,'phone':15,'tab':0,'mouse':0}
for i in d:
    if d[(i>2)]:
        print(i)
t=(9,2,13,4,5,6)
#0 2 26 12 20 30
for i in range(len(t)):
    print(i*t[i])
names ={'subbu','naresh','dinesh','sahith','rushi','praneeth'}
for i in names:
    print(i.upper())'''
names ={'subbu','naresh','dinesh','sahith','rushi','praneeth'}
for i in names:
    print(i.casefold())
