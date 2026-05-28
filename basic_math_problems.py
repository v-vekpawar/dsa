import math
def count_digits_1(n):
    if n == 0:
        return 1
    else:
        count=0
        while n>0:
            n=n//10
            count+=1
        return count

def count_digits_2(n):
    # Initialize a variable 'cnt' to
    # store the count of digits.
    cnt = int(math.log10(n) + 1)

    # The expression int(math.log10(n) + 1)
    # calculates the number of digits in 'n'
    # and casts it to an integer.
    
    # Adding 1 to the result accounts
    # for the case when 'n' is a power of 10,
    # ensuring that the count is correct.
   
    # Finally, the result is cast
    # to an integer to ensure it is rounded
    # down to the nearest whole number.
    
    # Return the count of digits in 'n'.
    return cnt

def reverse_number(n):
    if n < 0:
        return -reverse_number(-n)
    rnum = 0
    while n>0:
        rnum = rnum*10 + n%10
        n=n//10
    return rnum

def is_palindrome(n):
    if n < 0:
        return False
    return n == reverse_number(n)

def gcd_1(a,b):
    gcd = 1
    for i in range(1,(min(a,b)+1)):
        if a%i==0 and b%i==0:
            gcd = i
    return gcd

def gcd_2(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i
    return 1

def gcd_3(a, b):
    # euclidean algorithm to find GCD of a and b
    # Continue loop as long as both
    # a and b are greater than 0
    while a > 0 and b > 0:
        # If a is greater than b,
        # subtract b from a and update a
        if a > b:
            # Update a to the remainder
            # of a divided by b
            a = a % b
        # If b is greater than or equal
        # to a, subtract a from b and update b
        else:
            # Update b to the remainder
            # of b divided by a
            b = b % a
    # Check if a becomes 0,
    # if so, return b as the GCD
    if a == 0:
        return b
    # If a is not 0,
    # return a as the GCD
    return a

def is_armstrong(n):
    ndigits = count_digits_2(n)
    sum = 0
    temp = n
    while temp>0:
        digit = temp%10
        sum += digit ** ndigits
        temp=temp//10
    return sum == n

def all_divisors(n):
    divisors=[]
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
    return divisors

def getDivisors(self, N):
    # Create list to store divisors
    res = []

    # Loop from 1 to square root of N
    for i in range(1, int(math.isqrt(N)) + 1):
        # Check if i divides N
        if N % i == 0:
            # Add i to result
            res.append(i)

            # If N // i is not the same, add that too
            if i != N // i:
                res.append(N // i)

    # Return the list of divisors
    return res

def is_prime_1(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def is_prime_2(n):
    # 1. Handle the easy cases first
    if n < 2:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Exclude all other even numbers instantly

    # 2. Loop through odd numbers only, up to the square root
    # We start at 3 and step by 2 (3, 5, 7, 9, etc.)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False  # Found a factor, not prime

    return True