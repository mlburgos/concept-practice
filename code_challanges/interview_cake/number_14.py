# dont assume the list is sorted

l = [1,2,3,4,7,8,9,11,12]

################################################################################
# brut force
# O(n**2)

def watch_movies(flight, movie_lengths):

    for i, length_a in enumerate(movie_lengths):
        for j, length_b in enumerate(movie_lengths[i + 1:]):
            if length_a + length_b == flight:
                return True

    return False



################################################################################
# attempt 2
# O(n)

def watch_movies(flight, movie_lengths):

    dict_of_lengths = {}

    for i, length in enumerate(movie_lengths):
        dict_of_lengths[length] = dict_of_lengths.get(length, [])
        dict_of_lengths[length].append(i)

    print 'dict_of_lengths:', dict_of_lengths

    for length, indeces in dict_of_lengths.items():
        difference = flight - length

        if length == difference:
            if len(indeces) > 1:
                return True
        elif flight - length in dict_of_lengths:
            return True

    return False


################################################################################
# attempt 3: putting all in a sigle loop
# O(n)

def watch_movies(flight, movie_lengths):

    dict_of_lengths = {}

    for i, length in enumerate(movie_lengths):
        dict_of_lengths[length] = dict_of_lengths.get(length, [])
        dict_of_lengths[length].append(i)

        indeces = dict_of_lengths[length]

        print dict_of_lengths

        difference = flight - length

        if length == difference:
            if len(indeces) > 1:
                return True
        elif flight - length in dict_of_lengths:
            return True

    return False


################################################################################
# Interview cake solution: better than mine cuz they use a set so less memory
# required

def inflight_entertainment(flight, movie_lengths):

    set_of_lengths = set()

    for length in movie_lengths:
        second_movie = flight - length

        if second_movie in set_of_lengths:
            return True

        set_of_lengths.add(length)

    return False















































