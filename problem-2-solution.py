def fin(n):
    """

    :param n: the position of the number in Fibonacci sequence
    :return:
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fin(n-1) + fin(n-2)

def infinity(start=0):
    x = start
    while True:
        yield x
        x += 1

for n in infinity(1):
    """
    find the nth number whose value is exceeds 4,00,0000 
    """
    if fin(n) > 4000000:
        break
print(n)

result = 0

for n in range(1, 33):
    fib = fin(n)
    if (fib % 2) == 0:
        result += fib

print(result)

