# [1] => [[1],
#         ]
#
# [1,2] => [[1,2],
#           [2,1],
#           ]
#
# [1,2,3] => [[1,2,3],
#             [1,3,2],
#             [2,1,3],
#             [2,3,1],
#             [3,1,2],
#             [3,2,1],
#             ]
#
# given list of length n, get n! results


def permutations(lst):

    if lst == []:
        return []

    if len(lst) == 1:
        return lst

    all_permutations = []

    for i in range(len(lst)):

        sub_permutations = []
        start = lst[i]

        new_lst = lst[0:i] + lst[i+1:]

        lower_permutations = permutations(new_lst)

        for perm in lower_permutations:
            if type(perm) is int:
                sub_permutations.append([start] + [perm])
            else:
                sub_permutations.append([start] + perm)

        all_permutations.extend(sub_permutations)

    return all_permutations

################################################################################


def permutations(lst):

    if lst == []:
        return []

    if len(lst) == 1:
        return lst

    all_permutations = []

    for i in range(len(lst)):

        start = lst[i]

        new_lst = lst[0:i] + lst[i+1:]

        lower_permutations = permutations(new_lst)

        for perm in lower_permutations:
            if type(perm) is int:
                all_permutations.append([start] + [perm])
            else:
                all_permutations.append([start] + perm)

    return all_permutations
