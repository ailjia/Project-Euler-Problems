def palindromic(a, b, c):
    result = a * 10 ** 5 + b * 10 ** 4 + c * 10 ** 3 + c * 10 ** 2 + b * 10 + a * 1
    return result

_list = []

for a in range(10):
    for b in range(10):
        for c in range(10):
            _list.append(palindromic(a, b, c))

largest =  max(_list)

print(largest)
