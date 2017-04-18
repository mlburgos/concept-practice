# fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)

# def fibonacci(n):

#     if n == 0:
#         return 0

#     if n == 1:
#         return 1

#     return fibonacci(n-1) + fibonacci(n-2)

###############################################################################
# optimized solution
# ~~~~~~~not done ~~~~~~~~

def _fibonacci(n, memo):
    if n == 0 or n == 1:
        return n

    if memo[n] == 0:
        memo[n] = _fibonacci(n - 1, memo) + _fibonacci(n - 2, memo)

    return memo[n]

def fibonacci(n):

    return _fibonacci(n, [0] * (n + 1))
