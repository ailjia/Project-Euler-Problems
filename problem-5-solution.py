"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math
import time
start_time = time.time()

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

## get all the primes that are from 2 to 20
prim = [i for i in range(2, 21) if check_prim(i) == True]

result = 1

for j in prim:
    divisor = [i for i in range(20, 1, -1) if math.log(i, j).is_integer() == True]
    max_divisor = max(divisor)
    result *= max_divisor

print(result)

print("--- %s seconds ---" % (time.time() - start_time)) #--- 0.000125169754028 seconds ---
