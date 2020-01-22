"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

n = 600851475143

def check_prim(n):
    """

    :param n: to check if a number n is a prime number
    :return: return True if it is prime, false if it is not a prime
    """
    def check_no_prim(n):
        for divisor in range(2, n):
            if n % divisor == 0:
                return 'not prime' # not a prime

    if check_no_prim(n) == 'not prime':
        return False
    else:
        return True

def divide_loop(n):

    prim = []
    for i in range(10000, 2, -1):
        if check_prim(i) == True:
            prim.append(i)

    divisor = []
    quotient = n
    for prim in prim:
        if n % prim == 0:
            divisor.append(prim)
            quotient /= prim
    return divisor, max(divisor), quotient # result stored in a tuple

print(divide_loop(n)[1]) # print the max prime divisor