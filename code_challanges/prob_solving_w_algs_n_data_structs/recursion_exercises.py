# 1. write a recusive function to compute the factorial of a number


def rec_fact(num):
    if num == 1:
        return 1

    return num * rec_fact(num - 1)

# 2. write a recursive function to reverse a list

def rev_list(lst):
    if len(lst) == 1:
        return lst

    return [lst[-1]] + rev_list(lst[:-1])

