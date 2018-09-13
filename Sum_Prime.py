import math

def is_prime(number):
    k = math.ceil(math.sqrt(number)) + 1
    for i in range(2, k+1):
        if number % i == 0:
            return False

    return True

sum = 5

for i in range(3,2000000,2):
    #print(i)
    if is_prime(i):
        #print(i)
        sum +=i

print(sum)