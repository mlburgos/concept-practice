# given a 2 by 2 matrix, print items in spiral order

# given [[1,2],
#        [3,4]
#        ]

# print 1 2 4 3

block = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16],
         ]


block2 = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]
         ]


def spiral_print(array):

    # r = starting row
    # c = starting column
    # m = max row
    # n = max column

    r = 0
    c = 0
    m = len(array)
    n = len(array[0])

    while r < m and c < n:

        i = 0
        while i < n:
            print '[' + str(r) + '][' + str(c) + ']',
            print array[r][c]
            c += 1
            i += 1

        # back c up cuz if it exits the loop its gone too far
        c -= 1

        # since we've traversed the entire row, reduce number of rows
        m -= 1

        r += 1
        i = 0
        while i < m:
            print '[' + str(r) + '][' + str(c) + ']',
            print array[r][c]
            r += 1
            i += 1

        r -= 1
        n -= 1

        i = 0
        while i < n:
            c -= 1
            print '[' + str(r) + '][' + str(c) + ']',
            print array[r][c]
            i += 1

        m -= 1

        i = 0
        while i < m:
            r -= 1
            print '[' + str(r) + '][' + str(c) + ']',
            print array[r][c]
            i += 1

        n -= 1
        c += 1

        print 'm', m
        print 'n', n
