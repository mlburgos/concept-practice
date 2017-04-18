# Given the list of IDs, which contains many duplicate integers and one unique
# integer, find the unique integer.


# first attempt
# O(n) runtime, O(n) space

ids = [1,2,3,4,5,6,7,5,4,2,3,1,7]
# should return 6

def find_the_missing_drone(ids):

    tracker = set()
    for id in ids:
        if id in tracker:
            tracker.remove(id)
        else:
            tracker.add(id)

    return tracker.pop()



# Interiew Cake way
# also O(n) runtime, but has O(1) space by using bits

def missing_drone(ids):

    missing_id = 0
    print 'missing_id:', missing_id

    for id in ids:

        print 'id:', "{0:b}".format(id)

        missing_id ^= id

        print 'missing_id in bin:', "{0:b}".format(missing_id)
        print 'missing_id:', missing_id

    return missing_id