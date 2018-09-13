import numpy as np

r , c = input().split(' ')
r = int(r)
c = int(c)
#a = input().strip().split()
a = np.array([input().split() for _ in range(r)],dtype = float)
b = np.array([input().split(' ') for _ in range(r)],dtype = float)
print(a)
print(b)
print(a.shape)
print(b.shape)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)