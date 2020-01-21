def sum_multiples(n, a, b):
    """

    :param n: the integer threshod, in this case, 1000
    :param a: one of the multiples, in this case, 3
    :param b: one of the multiples, in this case, 5
    :return: sum of the multiples
    """

    a_n = (n-1) / a # number of multiples of a within n
    b_n = (n-1) / b # number of multiples of b within n

    def sum(a_n):
        if a_n == 1:
            return a
        else:
            return sum(a_n-1) + (a + a * (a_n - 1))

    def sum(b_n):
        if b_n == 1:
            return b
        else:
            return sum(b_n - 1) + (b + b * (b_n - 1))

    result = sum(a_n) + sum(b-n)
    return result

