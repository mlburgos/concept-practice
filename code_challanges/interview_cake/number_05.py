# given change=4, coins = [1,2,3]
# retrun 4, the number of dif combos of coins that add up to change

def make_change(change, coins):

    # Base case
    # if change == 0:
    #     return 1
    # elif change < 0:
    #     return 0
    if change in coins:
        return 1

    # Goal: end up returning a count.
    count = 0

    for coin in coins:
        print 'coin:', coin
        count += make_change(change - coin, coins)

    print 'adding extra to count'
    return count 

################################################################################
# But we want unique change combos

4 => {[1,1,1,1],
      [1,1,2],
      [1,3],
      [2,2]
      }

5 => {[1,1,1,1,1],
      [1,1,1,2],
      [1,1,3],
      [1,2,2],
      [2,3],
      }

6 => {[1,1,1,1,1,1],
      [1,1,1,1,2], 
      [1,1,1,3],
      [1,1,2,2]
      [1,2,3],
      [2,2,2],
      [3,3],
      }
     

# def number_of_ways(amount, denominations):
#     answer = 0
#     for each denomination in denominations:
#         for each num_times_to_use_denomination in possible_num_times_to_use_denomination_without_overshooting_amount:
#             answer += number_of_ways(amount_remaining, other_denominations)
#     return answer


def make_change(change, coins):

    return _make_change(change, coins, None)


def _make_change(remaining, coins, idk=None):
    if remaining == 0:
        return 1

    if remaining < 0:
        return 0

    answer = 0

    for i, coin in enumerate(coins):

        for j in range(remaining/coin):
            answer += _make_change(remaining - coin, coins[:i] + coins[i+1:])

    return answer


