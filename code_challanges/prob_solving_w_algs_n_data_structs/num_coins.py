# Given a list of coin options, and a desired amount of change, find the fewest
# number of coins necessary to make the change

US_COINS = [25, 10, 5, 1]

#  first attempt: success!

def min_coins1(coin_val_list, change):

    # Base case: change amount equals a coin option
    if change in coin_val_list:
        # print "change is in coin_val_list"
        return 1

    combos = []

    for coin in coin_val_list:
        if change >= coin:
            # print "coin:", coin
            # print "change:", change
            combos.append(1 + min_coins1(coin_val_list, change - coin))

    # print "combos:", combos
    return min(combos)


# second attempt: done after understanding the code in the book

def min_coins2(coin_val_list, change):

    # initializing the min_num by assigning it to the change sets it as its
    # greatest possible value (i.e. the number of pennies required to make that
    # change amount)
    min_num = change

    # Base case: change amount equals a coin option
    if change in coin_val_list:
        return 1

    for coin in coin_val_list:
        if change >= coin:
            num_coins = 1 + min_coins2(coin_val_list, change - coin)

            if num_coins < min_num:
                min_num = num_coins

    return min_num


# pretty much from the book pg177 Listing 4.14

def min_coin3(coin_val_list, change):
    min_coins = change

    if change in coin_val_list:
        return 1
    else:
        for coin in [c for c in coin_val_list if c <= change]:
            num_coins = 1 + min_coin3(coin_val_list, change - coin)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


########################################################################
# Optimized using memoization
#############
# I changed the indeces to be 'change - 1' instead of 'change' which is what the 
# book uses. 'Change' caused out of rancge errors

def opt_min_coins(coin_val_list, change, known_mins):
    min_coins = change
    if change in coin_val_list:
        known_mins[change - 1] = 1
        return 1
    elif known_mins[change - 1] > 0:
        return known_mins[change - 1]
    else:
        for coin in [c for c in coin_val_list if c <= change]:
            num_coins = 1 + opt_min_coins(coin_val_list, change - coin, known_mins)
            if num_coins < min_coins:
                min_coins = num_coins
                known_mins[change - 1] = min_coins

    print known_mins
    return min_coins


opt_min_coins([1,5,10,25], 63, [0]*63)



































