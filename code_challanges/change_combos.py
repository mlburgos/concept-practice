# You have an endless supply of dimes and pennies. How many different amounts
# of total change can you make using exactly num_coins number coins?
# For example, when num_coins = 3, you can create 4 different kinds of change:
# • 3 cents from penny + penny + penny
# • 12 cents dime + penny + penny
# • 21 cents from dime + dime + penny
# • 30 cents from dime + dime + dime

# So, you should have a function that returns the set {3,12,21,30} when num_coins is 3.

# >>> coins(1) == ([1, 10]) True
# >>> coins(2) == ([2, 11, 20]) True
# >>> coins(3) == ([3, 12, 21, 30]) True
# >>> coins(4) == ([4, 13, 22, 31, 40]) True
# >>> coins(10) == ([10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100]) True


coin_types = [1, 10]


def coins(n):
    memo = [0] * (n + 1)

    return _coins(remaining_coins=n, memo=memo)


def _coins(remaining_coins, memo):
    if remaining_coins == 0:
        return set([0])

    if memo[remaining_coins] == 0:
        change_ops = set()

        prior_change_ops = _coins(remaining_coins - 1,
                                  memo)

        for op in prior_change_ops:
            for coin_type in coin_types:
                change_ops.add(coin_type + op)

        memo[remaining_coins] = change_ops

    return memo[remaining_coins]
