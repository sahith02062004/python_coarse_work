'''def function_name(arg):
#stmts
return
 
function_name(para)
def wish(wish):
    print(f'Welcome to the python course {name}!')
wish('sahith')
wish('subbu')
wish('praneeth')

def iseven(num):
    if num%2==0:
        return f"{num} - Even Number"
    else:
        return f"{num} - Odd Number"
num=int(input("Enter the number"))
print(iseven(num))

#Factorial
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num = int(input("Enter the number: "))
print(factorial(num))

def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - Nor Prime Number"
    return f"{num} - Prime Number"
num = int(input("Enter the number: "))
print(isprime(num))
#oosition
def display(name,email,password):
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)
display("sahith","sahithsriramoju@gmail.com","sahith@123")
display("sahithsriramoju@gmail.com","sahith","sahith@123")
display("sahith@123","sahith","sahithsriramoju@gmail.com")

#keyword
def display(name,email,password):
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)
display(name="sahith",email="sahithsriramoju@gmail.com",password="sahith@123")
display(email="sahithsriramoju@gmail.com",name="sahith",password="sahith@123")
display(password="sahith@123",name="sahith",email="sahithsriramoju@gmail.com")

#default=" " or ' ' should be at end for only email=' ' and password=' ' but not for starting name
def display(name,email,password=" "):
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)
display("sahith","sahithsriramoju@gmail.com","sahith@123")
display("sahith","sahithsriramoju@gmail.com")

#variable positional
def display(*names):
    print("Names:",names)
display('sahith','dinesh','naresh','akhil','nagendra')
display('naresh','akhil','nagendra')
display('subbu','dinesh','naresh','akhil')
display('nagendra')
display('subbu','dinesh')
'''
def display(**names):
    print("Names:",names)
display(k1='sahith',k2='dinesh',k3='naresh')
display(k1='naresh')
display(k1='subbu',k2='dinesh')

