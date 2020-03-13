def sum_multiples(n, a, b):
    """

    :param n: the integer threshod, in this case, 1000
    :param a: one of the multiples, in this case, 3
    :param b: one of the multiples, in this case, 5
    :return: sum of the multiples
    """

    a_n = (n - 1) / a  # number of multiples of a within n
    b_n = (n - 1) / b  # number of multiples of b within n

    def sum(a_n, a):
        if a_n == 0:
            pass
        if a_n == 1:
            return a
        else:
            return sum(a_n - 1, a) + a + a * (a_n - 1)

    result = sum(a_n, a) + sum(b_n, b)
    return result

(n, a, b) = tuple(input('what are the values of n, a, and b?'))
print(sum_multiples(n, a, b))
