# Suppose we had a list ↴ of nn integers sorted in ascending order. How quickly
# could we check if a given integer is in the list?

l = [2,3,5,6,8,9,13,17]
n1 = 4
n2 = 13

# binary search 

def contians_num(intr, nums):

    if nums == []:
        return False

    mid_i = len(nums)/2
    mid = nums[mid_i]

    if mid == intr:
        return True
    elif mid < intr:
        return contians_num(intr=intr,
                            nums=nums[mid_i+1:])
    else:
        return contians_num(intr=intr,
                            nums=nums[:mid_i])



###############################################################################
# itterative implementation

def cont_num(intr, nums):

    # we think of floor_index and ceiling_index as "walls" around
    # the possible positions of our target, so by -1 below we mean
    # to start our wall "to the left" of the 0th index
    # (we *don't* mean "the last index")
    
    floor_index = -1
    ceiling_index = len(nums)

    # if there isn't at least 1 index between floor and ceiling,
    # we've run out of guesses and the number must not be present

    while floor_index + 1 < ceiling_index:
        print 'floor_index:', floor_index
        print 'ceiling_index:', ceiling_index

        mid_of_range = floor_index + (ceiling_index - floor_index)/2

        print 'nums[mid_of_range]:', nums[mid_of_range]

        if nums[mid_of_range] == intr:
            return mid_of_range

        elif nums[mid_of_range] < intr:
            floor_index = mid_of_range

        else:
            ceiling_index = mid_of_range

    return 'not in list'

