#  given n, return a list of the Fibonacci seq of that length
# [1 ,1, 2, 3, 5, 8 ]


# Done recursively:

def gen_fibonacci(n, fib_list=[]):

    if len(fib_list) == n:
        return fib_list

    if n <= 2:
        return [1]*n

    if fib_list == []:
        fib_list = [1]*2

    fib_list.append(fib_list[-1] + fib_list[-2])

    return gen_fibonacci(n, fib_list)


# Done iteratively:
def iter_gen_fibonacci(n):

    fib_list = []

    for i in range(n):
        print '{} fib_list:'.format(i), fib_list
        if i <= 1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[-2] + fib_list[-1])

    return fib_list

