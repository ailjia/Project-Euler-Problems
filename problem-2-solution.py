import itertools

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

for n in itertools.count(1)  #infinity(1)
    """
    find the nth number whose value is exceeds 4,00,0000 
    """
    if fin(n) > 4000000:
        break

print(n)

# for the sequence of the Fibonacci number positioned from 1 to n-1, apply the fin() to get the number
# and keep the number in a list l if that number is even

l = [fin(i) for i in range(1,n) if (fin(i) % 2) == 0 ]

print(sum(l))
