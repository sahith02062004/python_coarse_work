n = 9
'''n=int(input())
m=n//2
for i in range(n):
    if i<m:
        for j in range(i+1):
            print('*',end="")
    else:
        for j in range(n-i):
            print('*',end="")
    print()

n=int(input())
m=n//2
for i in range(n):
    if i<m:
        for j in range(i+1):
            print('*'*(i+1),end="")
    else:
        for j in range(n-i):
            print('*'*(n-i), end="")
    print()

n=int(input())
m=n//2
for i in range(n):
    if i<m:
        for j in range(i+1):
            print('*',end="")
    else:
        for j in range(n-i):
            print('*',end="")
   print()
n=int(input())
m=n//2
for i in range(n):
    if i<m:
        for j in range(i+1):
            print('*',end="")
    else:
        for j in range(n-i):
            print('*',end="")
    print()

n=int(input())
m=n//2
for i in range(n):
    if i<m:

        print(' '*(m-i)+'* '*(i+1),end="")
    else:

        print(' '*(i-m)+'* '*(n-i),end="")
    print()

n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
n=int(input())
m=n//2
for i in range(n):
    if i<m:
        for j in range(i+1):
            print('*',end="")
    else:
        for j in range(n-i):
            print('*',end="")
    print()


n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or j==i or i+j==n-1 or i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#A
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==m:
            print('*',end=' ')
        else:
            print(' ' ,end=' ')
    print()
'''
#B
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (j==n-1 and i<=n//2) or (i==n//2 and j>=n//2):
            print('*',end=' ')
        else:
            print(' ' ,end=' ')
    print()




