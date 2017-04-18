stock_prices_yesterday = [10, 7, 5, 8, 11, 9]


def get_max_profit(stock_prices_yesterday):
    """ Returns 6 (buying for $5 and selling for $11)
    """

    differences = []

    for i in xrange(len(stock_prices_yesterday) - 1):
        next_dif = stock_prices_yesterday[i + 1] - stock_prices_yesterday[i]
        if differences and differences[-1] > 0 and next_dif > 0:
            differences[-1] += next_dif
        else:
            differences.append(next_dif)

    return max(differences)

    # differences = [-3, -2, 6, -2]
    # maxi = differences[0]
    # for dif in differences:
    #     if dif > maxi:
    #         maxi = dif
    # return maxi

    # OR


  def get_max_profit(stock_prices_yesterday):

    min_price = stock_prices_yesterday[0]
    max_profit = None

    for current_price in stock_prices_yesterday:

        # ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        if max_profit is None:
            max_profit = potential_profit
        else:
            max_profit = max(max_profit, potential_profit)

    return max_profit

    