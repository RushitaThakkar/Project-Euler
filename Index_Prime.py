import math

def is_prime(number):
    k = math.ceil(math.sqrt(number)) + 1
    for i in range(2, k+1):
        if number % i == 0:
            return False

    return True

def index_prime(n):

    prime_index = 1
    i = 1
    while prime_index < n:
        if is_prime(i):
            prime_index +=1

        i +=1

    return (i-1)

print(index_prime(10001))
