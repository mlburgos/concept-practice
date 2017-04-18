# given:   [1, 7, 3, 4]
# return:   [84, 12, 28, 21]
# by doing:   [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]


def product(numbers):
    prod = 1

    for num in numbers:
        prod *= num

    return prod


def list_prod(numbers):
    products = []

    for i in xrange(len(numbers)):
        products.append(product(numbers[:i] + numbers[i + 1:]))

    return products

################################################################################
# Trying for O(n) time and space


def list_prod(numbers):
    products = [1]*len(numbers)

    prod_before = 1
    prod_after = 1
    for i, num in enumerate(numbers):
        products[-(i + 1)] *= prod_after

        products[i] *= prod_before

        prod_before *= num
        prod_after *= numbers[-(i + 1)]

    return products


################################################################################
# Allowing division

def list_prod_division(numbers):

    prod = 1
    zero_index = None

    for index, num in enumerate(numbers):
        if num != 0:
            prod *= num
        elif zero_index is not None:
            return [0] * len(numbers)
        else:
            zero_index = index

    if zero_index:
        products = [0]*len(numbers)
        products[zero_index] = prod
        return products

    products = [prod] * len(numbers)

    for index, num in enumerate(numbers):
        products[index] = prod/num

    return products

