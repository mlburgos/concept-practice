q = [-1, -10, 2, 3, -10, 2]


def find_largest_three(ints):
    # find the order of the first three ints. Make max1 the largest

    if ints[0] > ints[1]:
        if ints[0] > ints[2]:
            max1 = ints[0]
            if ints[1] > ints[2]:
                max2 = ints[1]
                max3 = ints[2]
            else:
                max2 = ints[2]
                max3 = ints[1]
        else:
            max1 = ints[2]
            max2 = ints[0]
            max3 = ints[1]

    if ints[1] > ints[0]:
        if ints[1] > ints[2]:
            max1 = ints[1]
            if ints[0] > ints[2]:
                max2 = ints[0]
                max3 = ints[2]
            else:
                max2 = ints[2]
                max3 = ints[0]
        else:
            max1 = ints[2]
            max2 = ints[1]
            max3 = ints[2]

    if ints[2] > ints[1]:
        if ints[2] > ints[0]:
            max1 = ints[2]
            if ints[1] > ints[0]:
                max2 = ints[1]
                max3 = ints[0]
            else:
                max2 = ints[0]
                max3 = ints[1]
        else:
            max1 = ints[0]
            max2 = ints[2]
            max3 = ints[1]

    return [max1, max2, max3]

# O(n) time O(1) space

def product_of_largest_three(ints):
    max1, max2, max3 = find_largest_three(ints[:3])
    sml1 = max3
    sml2 = max2

    for i, num in enumerate(ints):
        if i < 3:
            continue

        if num > max1:
            max1, max2, max3 = num, max1, max2
        elif num > max2:
            max2, max3 = num, max2
        elif num > max3:
            max3 = num
        elif num < sml1:
            sml1, sml2 = num, sml1
        elif num < sml2:
            sml2 = num

    return max(max1*max2*max3, sml1*sml2*max1)



################################################################################
# O(n log n)


def product_of_largest_three(ints):

    ints.sort()

    return ints[-1] * ints[-2] * ints[-3]

################################################################################
# accounting for negatives
# O(n log n)


def product_of_largest_three(ints):

    ints.sort()

    return  max(ints[-1] * ints[-2] * ints[-3], ints[0] * ints[1] * ints[-1])


################################################################################
# Interview cake solution
# O(n) time O91) space

def product_of_largest_three(ints):
    highest = max(ints[0], ints[1])
    lowest = min(ints[0], ints[1])

    highest_of_two = ints[0] * ints[1]
    lowest_of_two = ints[0] * ints[1]

    highest_of_three = highest_of_two * ints[2]

    for i, num in enumerate(ints):
        if i < 3:
            continue

        possible_highest_of_three = max(highest_of_two * num,
                                        lowest_of_two * num)

        highest_of_three = max(possible_highest_of_three, highest_of_three)

        lowest_of_two = min(lowest_of_two, lowest * num)
        lowest = min(lowest, num)

        highest_of_two= max(highest_of_two, highest*num)
        highest = max(highest, num)


    return highest_of_three
    




