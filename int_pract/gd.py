def  countDuplicates( numbers):
    counts_by_number = {}

    for number in numbers:
        counts_by_number[number] = counts_by_number.get(number, 0) + 1

    non_unique_count = 0

    for count in counts_by_number.values():
        if count > 1:
            non_unique_count += 1

    return non_unique_count

a = [1,3,1,4,5,6,3,2]


###############################################################################

def  buildSubsequences( s):

    sub_seqs = []

    for i in range(len(s)):
        current_letter = s[-(i + 1)]
        sub_seqs.append(current_letter)

        for seq in sub_seqs[:-1]:
            sub_seqs.append(current_letter + seq)


    return sorted(sub_seqs)

s = 'abc'

==>
a
ab
abc
ac
b
bc
c


###############################################################################

def arrangeCoins(coins):

    result = []
    known_values = []

    for coin in coins:
        sub_result, known_values = _arrangeCoins(coin, known_values)

        result.append(sub_result)

    return result


def _arrangeCoins(coin, known_values):

    if len(known_values) > coin:
        return [known_values[coin], known_values]

    coins_to_add = 1
    n_steps = 0
    needed_coins = 0

    for i in range(coin + 1):
        if i >= needed_coins + coins_to_add:
            n_steps += 1
            needed_coins += coins_to_add
            coins_to_add += 1
        if i >= len(known_values):
            known_values.append(n_steps)

    return [n_steps, known_values]


###############################################################################

def _arrangeCoins(coin, known_values):
    # Helper function to update known_values and return step count
 
    if len(known_values) > coin:
        print known_values[coin]
        return [known_values[coin], known_values]

    needed_coins = 0

    if known_values:
        coins_to_add = known_values[-1] + 1
        n_steps = known_values[-1]
        for i in range(n_steps + 1):
            needed_coins += i
    else:
        coins_to_add = 1
        n_steps = 0

    for i in range(len(known_values), coin + 1):
        if i >= needed_coins + coins_to_add:
            n_steps += 1
            needed_coins += coins_to_add
            coins_to_add += 1
        if i >= len(known_values):
            known_values.append(n_steps)

    print n_steps
    return [n_steps, known_values]


def arrangeCoins(coins):
    
    result = []
    known_values = []

    for coin in coins:
        sub_result, known_values = _arrangeCoins(coin, known_values)

        result.append(sub_result)

    return result

###############################################################################



def rec_arrangeCoins(coin, step_lengths, sum_of_steps):
    
    coins_needed = 0 
    for i in range(len(step_lengths)):
        coins_needed += i
        next_step = coins_needed + i
        if coin >= coins_needed and coin < next_step:
            return step_lengths[i]


###############################################################################

def arrangeCoins(coins):
    


    for coin in coins:
        print _rec_arrangeCoins(coin)
ß

def _rec_arrangeCoins(coin, step_length=1):

    if coin < step_length:
        return 0

    return 1 + _rec_arrangeCoins(coin - step_length, step_length + 1)


###############################################################################

def arrangeCoins(coins):

    known_values = [0]*(max(coins) + 1)

    for coin in coins:
        print _rec_arrangeCoins(coin, known_values)


def _rec_arrangeCoins(coin, known_values):

    
    if known_values[coin] == 0:
        known_values[coin] = 


###############################################################################

def arrangeCoins(coins):
    memo = [0]*(max(coins) + 1)

    print memo
    for coin in coins:
        print _rec_arrangeCoins(remaining_coins=coin,
                                next_step=0,
                                memo=memo,
                                initial_coins=coin,
                                )


def _rec_arrangeCoins(remaining_coins, next_step, memo, initial_coins):

    print memo

    if remaining_coins < next_step:
        return next_step - 1

    memo[initial_coins] = _rec_arrangeCoins(remaining_coins=remaining_coins - next_step,
                                            next_step=next_step + 1,
                                            memo=memo,
                                            initial_coins=initial_coins,
                                            )

    return memo[initial_coins]
