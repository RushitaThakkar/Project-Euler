def sum_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2

    return sum

def square_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
        square = sum**2

    return square

a = sum_squares(100)
b = square_sum(100)

diff = b - a

print(int(diff))