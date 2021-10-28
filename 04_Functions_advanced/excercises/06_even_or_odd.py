def even_odd(*args):
    nums = list(args[:-1])
    if args[-1] == 'odd':

        return [int(el) for el in nums if el % 2 ==1]
    return [int(el) for el in nums if el % 2 ==0]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
