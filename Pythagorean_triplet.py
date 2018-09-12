import math
import time


def is_pythagorean(a,b,c):

    if (a**2 == b**2 + c**2):
        return True

    else:
        return False

start = time.time()
for i in range(1,1000):
    for j in range(i+1, 1000):
        k = 1000-i-j
        if is_pythagorean(k,j,i):
            print(i*j*k)

print("--- %s seconds ---" % (time.time() - start))





