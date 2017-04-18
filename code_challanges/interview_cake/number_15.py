# Write a function fib() that a takes an integer nn and returns the nnth
# fibonacci ↴ number.
# Let's say our fibonacci series is 0-indexed and starts with 0.


def fib(n):
    memo = [0] * (n + 1)
    memo[1] = 1

    return _fib(n, memo)


def _fib(n, memo):

    if n == 0:
        return 0
    elif memo[n] > 0:
        return memo[n]

    if memo[n - 1] > 0:
        memo[n] = memo[n-1] + memo[n-2]
    else:
        memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)

    print memo
    return memo[n]



################################################################################
# Attempt 2: aiming for constant space

def fib(n):

    if n == 0:
        return 0

    current = 1
    prior = 1
    priors_prior = 0

    for i in xrange(2, n + 1):
        current = prior + priors_prior

        priors_prior = prior
        prior = current

    return current




