# given change = 10
# coins = [1,2,3]
#
# return number of different coin combos to make change


def make_change(change, coins):

    tracker = [0]*(change + 1)

    # base case: there's only one way to make 0
    tracker[0] = 1

    for coin in coins:
        for amount in range(coin, change + 1):
            tracker[amount] += tracker[amount - coin]

        print tracker

    return tracker[change]
