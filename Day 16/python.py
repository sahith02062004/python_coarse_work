'''
#localScope
def display():
    n=10
    print("Inside:",n)
display()
#print("Outside:",n) the program will run no error if keep #

#global access
n=10
def display():
    print("Inside:",n)
display()
print("Outside:",n)

def display():
    global n
    n=10
    print("Inside:",n)
display()
print("Outside:",n)

def display():
    global n
    n+=10
    print("Inside:",n)
n=10
display()
print("Outside:",n)

def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Outer function:",n)
    inner()
    print("Outer function:",n)
outer()

s='python'
print(len(s))
len=5
print(len(s))

#int float complex str list tuple set dict
#int float complex str tuple bool
#list set dict
def update(n):
    n=1,2,3
    print("Inside:",n)
n=4,5,6
update(n)
print("Outside:",n)

def update(n):
    n.add(6,7)
    print("inner function:",n)
n=(1,2,3,4,5)
print("Outer function:",n)

def update(n):
    n.append(6,7)
    print("inner function:",n)
n=[1,2,3,4,5]
print("Outer function:",n)

#recursion
def func():
    if basecondition:
        return
    func()

def func(num):
    if num==0:
        return
    print(num,end=' ')
    func(num-1)
func(5)

def func(num):
    if num==0:
        return
    print(num,end=' ')
    func(num-1)
    print(num,end=' ')

def func(num):
    if num==0:
        return
   # print(num,end=' ')
    func(num-1)
    print(num,end=' ')
func(5)

def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(5))

def sumofdigits(n):
    if n==0:
        return 1
    return n*sumofdigits(n-1)
print(sumofdigits(5))

def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,4))
print(power(3,3))
'''
def reverseofstr(s,ind):
    if ind==0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)
l="Python Programming"
print(reverseofstr(l,len(l)-1))
