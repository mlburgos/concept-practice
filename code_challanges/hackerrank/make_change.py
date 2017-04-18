# Attempt 1: too slow

def make_change(coins, n):
    if n == 0:
        return 1

    count = 0 

    for i in range(len(coins)): 
        if n - coins[i] >= 0:
            count += make_change(coins[i:], n - coins[i])

    return count


################################################################################
# Attempt 2: use memoization

def _make_change(coins, n, memo):
    if n == 0:
        return 1

    if memo[n] == 0:

        count = 0 

        for i in range(len(coins)): 
            if n - coins[i] >= 0:
                count += _make_change(coins[i:], n - coins[i], memo)
        
        memo[n] = count
    print 'memo:', memo
    return memo[n]


def make_change(coins, n):
    memo = [0]*(n + 1)
    return _make_change(coins, n, memo)



################################################################################
# modified solutiobn from internet

def make_change(coins, n):
    results = [0]*(n + 1)
    results[0] = 1
    for coin in coins:
        print 'coin:', coin
        for i in range(coin, n + 1):
            results[i] += results[i - coin]
            print 'results:', results

    return results[n]

coins = [1,2,3]

n = 4

==> {1,1,1,1},
    {112}
    {22}
    {13}


# in my own words
def make_change(change, coins):
    tracker = [0] * (change + 1)

    # Base case: only one way to get 0
    tracker[0] = 1

    for coin in coins:
        for amount in range(coin, change + 1):
            tracker[amount] += tracker[amount - coin]

        print tracker

    return tracker[-1]


################################################################################
# method in CCI

def make_change(coins, n):
    return _make_change(coins, n, 0)

def _make_change(coins, n, index):
    if index >= len(coins):
        return 1

    coin = coins[index]

    ways = 0

    i = 0

    while i * coin <= n:
        remaining = n - i * coin
        ways += _make_change(coins, remaining, index + 1)
        i +=1

    return ways



