# fill 3 gal
# pour it into the 4 gal
# fill 3 gal
# pour into 4 gal until full
# dump for gal
# pour what remains in the 3 gal into the 4 gal

def get_2_gals(jug_1=0, jug_2=0):
    print "jug_1:", jug_1
    print "jug_2:", jug_2

    if jug_2 == 4:
        # empty jug_2
        jug_2 = 0
        print "jug_1:", jug_1
        print "jug_2:", jug_2

        jug_2 = jug_1
        jug_1 = 0

        print "jug_1:", jug_1
        print "jug_2:", jug_2

        return 'Jug_2 has {} galons'.format(jug_2)

    # fill jug_1
    jug_1 = 3

    print "jug_1:", jug_1
    print "jug_2:", jug_2

    # pour jug_1 into jug_2 until jug_2 is full or jug_1 is empty
    total_vol = jug_1 + jug_2

    if total_vol <= 4:
        jug_2 = total_vol
        jug_1 = 0
    else:
        jug_2 = 4
        jug_1 = total_vol - 4

    return get_2_gals(jug_1, jug_2)


