import math


def gen_counter(string):
    counter = {}

    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1

    return counter


def letter_dif(str1, str2):
    counter1 = gen_counter(str1)
    counter2 = gen_counter(str2)

    dif_sum = 0

    for key in counter1.keys():
        if key not in counter2:
            dif_sum += counter1[key]
        else:
            fabs = math.fabs(counter1[key] - counter2[key])
            dif_sum += fabs

    for key in counter2.keys():
        if key not in counter1:
            dif_sum += counter2[key]

    return dif_sum
