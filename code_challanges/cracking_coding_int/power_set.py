
def power_set(curr_set):
    if len(curr_set) == 0:
        return []

    curr = curr_set.pop()
    subsets = [{curr}]

    lower_subsets = power_set(curr_set)

    for subset in lower_subsets:
        subsets.append(subset)

        # make a copy to add the curr value so that the subset you already added
        # isn't mutated
        copy = set(subset)
        copy.add(curr)
        subsets.append(copy)

    return subsets


################################################################################
# better version: includes the empty set in the subsets

def power_set(curr_set):
    if len(curr_set) == 0:
        return [{}]

    curr = curr_set.pop()
    subsets = []

    lower_subsets = power_set(curr_set)

    for subset in lower_subsets:
        subsets.append(subset)

        # make a copy to add the curr value so that the subset you already added
        # isn't mutated
        copy = set(subset)
        copy.add(curr)
        subsets.append(copy)

    return subsets

set1 = {1,2,3,4}




