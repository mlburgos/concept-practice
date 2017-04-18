cake_tuples = [(7, 160), (3, 90), (2, 15)]
cake_tuples2 = [(7, 160), (3, 90), (2, 15), (1, 50)]
cake_tuples3 = [(7, 160), (3, 90), (2, 15), (0, 0)]
cake_tuples4 = [(3, 40), (5, 70)]

capacity = 20


################################################################################
# Attmept 1
# good try, but fials with cake_tuples4 and capacity=9

# def max_duffle_bag_value(cake_tuples, capacity):

#     max_money_per_kg = 0
#     max_money_per_kg_i = 0

#     for i, cake_tuple in enumerate(cake_tuples):
#         kg, worth = cake_tuple

#         if min(kg, worth) == 0:
#             continue

#         money_per_kg = float(worth)/kg
#         if money_per_kg > max_money_per_kg:
#             max_money_per_kg = money_per_kg
#             max_money_per_kg_i = i

#     weight_per_cake, value_per_cake = cake_tuples[max_money_per_kg_i]

#     max_quantity = (capacity / weight_per_cake)

#     added_value_to_duffle = max_quantity * value_per_cake

#     print 'max_money_per_kg:', max_money_per_kg
#     print 'added_value_to_duffle:', added_value_to_duffle

#     if capacity % weight_per_cake == 0:
#         return added_value_to_duffle

#     return (added_value_to_duffle +
#             max_duffle_bag_value(cake_tuples[:max_money_per_kg_i] +
#                                  cake_tuples[max_money_per_kg_i + 1:],
#                                  capacity - weight_per_cake * max_quantity)
#             )

################################################################################
# Attmept 2

def max_duffle_bag_value(cake_tuples, capacity):

    max_values = [0] * (capacity + 1)

    for current_capacity in xrange(1, capacity + 1):

        for kg, value in cake_tuples:
            if kg == 0:
                return float('inf')

            if kg <= current_capacity:
                # if value + max_values[current_capacity - kg] > max_values[current_capacity]:
                #     max_values[current_capacity] = value + max_values[current_capacity - kg]
                # OR
                max_values[current_capacity] = max(value
                                                   + max_values[current_capacity
                                                                - kg],
                                                   max_values[current_capacity],
                                                   )

    return max_values[capacity]
































