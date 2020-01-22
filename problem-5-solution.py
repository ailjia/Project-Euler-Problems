"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

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


prim = []

## get all the primes that are from 2 to 20
for i in range(2, 21):
    if check_prim(i) == True:
        prim.append(i)

lists = [[] for _ in range(len(prim))] # create multiple empty lists to store the numbers later

for i in range(20, 1, -1):
    for j in prim:
        if math.log(i, j).is_integer():
            lists[prim.index(j)].append(i)

print(lists)

result = 1
for list in lists:
    max_divisor = max(list)
    result *= max_divisor

print(result)

