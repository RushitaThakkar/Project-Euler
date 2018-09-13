def is_Palindrome(n):
    temp = n
    rev = 0
    dig = 0

    while n>0:
        dig = n%10
        rev = rev*10 + dig
        n = n//10

    if(temp==rev):
        return True
    else:
        return False

maxmul = 1
for i in range(100,1000):
    for j in range(100,1000):
        mul = i*j
        if is_Palindrome(mul):
            #print(i)
            #print(j)
            #print(mul)
            #print("****")
            if mul > maxmul:
                maxmul = mul

print(maxmul)

