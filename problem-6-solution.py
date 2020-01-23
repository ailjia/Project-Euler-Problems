def sum_squares(n):
    if n== 0:
        pass
    if n == 1:
        return 1
    else:
        return sum_squares(n-1) + n ** 2

def squares_sum(n):
    def sum(n):
        if n == 0:
            pass
        if n == 1:
            return 1
        else:
            return (sum(n-1) + n)
    return sum(n) ** 2