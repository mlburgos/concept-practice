# find the rotation point

# given 
l = ['pa', 'ra', 'ta', 'va', 'wa', 'za', 'ba', 'da']
# return index of rotation point (6)


words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

################################################################################
# attempt 1: brut force
# O(n)

def find_rotation_point(lst):
    # get the first letter of the first word
    test_letter = lst[0][0]

    for i, word in enumerate(lst):
        if i == 0:
            continue

        current = word[0]

        if ord(current) < ord(test_letter):
            return i

    return 'there is no pivot'


################################################################################
# attempt 2: aim for faster runtime
# O(lg(n)) !!!

def find_rotation_point(lst):
    # get the first letter of the first word
    test_letter = lst[0][0]

    return _find_rotation_point(words=lst, i_adj=0, test_letter=test_letter)


def _find_rotation_point(words, i_adj, test_letter):
    if words == []:
        return 'There is no pivot'

    mid_i = len(words)/2

    mid_first_letter = words[mid_i][0]

    if ord(mid_first_letter) > ord(test_letter):
        return _find_rotation_point(words=words[mid_i + 1:],
                                    i_adj=mid_i + 1,
                                    test_letter=test_letter,
                                    )

    elif ord(mid_first_letter) < ord(test_letter):
        # Case 1
        if mid_i == 0 or ord(mid_first_letter) < ord(words[mid_i - 1][0]):
            return mid_i + i_adj

        return _find_rotation_point(words=words[:mid_i],
                                    i_adj=i_adj,
                                    test_letter=test_letter,
                                    )

################################################################################
# Interview cake version (with my own words)

def rotation_point(words):

    first_word = words[0]

    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:

        mid_of_range = floor_index + (ceiling_index - floor_index)/2

        if words[mid_of_range] >= first_word:
            floor_index = mid_of_range
            continue

        ceiling_index = mid_of_range

        if floor_index + 1 == ceiling_index:
            return ceiling_index
