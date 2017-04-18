
def permutations(string):

    if string == "":
        return None
    elif len(string) == 1:
        return set(string)

    perms = set()

    for i in range(len(string)):
        char = string[i]
        sub_str = string[0:i] + string[i+1:]

        sub_perms = permutations(sub_str)

        for perm in sub_perms:
            perms.add(char + perm)

    # print 'perms:', perms
    return perms



################################################################################
# Incomplete
def gen_counts(string):
    """Given a string, return a dictionary where the unique letters are keys
    and values are the counts"""

    counts = {}
    for letter in string:
        counts[letter] = counts.get(letter, 0) + 1

    return counts

def dupes(string):
    counts = gen_counts(string)

    return _dupes(counts)


def _dupes(counts):
    perms = set()

    for letter, count in counts.items():
        if count > 0:
            sub_set = _dupes()