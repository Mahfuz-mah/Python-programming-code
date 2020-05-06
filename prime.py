def is_prime2(n):
    if n == 0:
     return True #2 is prime
    if n % 2 == 0:
     print(n,"is divisible by 2")
    return False  #even number is excepted 2 are not prime
    if n < 2:
    return False  # number is less than 2 are not prime
    prime =True
    for x in range(3,n,2):
     if n % x == 0:
    print(n,"is divisible by",x)
     prime = False
    return prime
    return prime