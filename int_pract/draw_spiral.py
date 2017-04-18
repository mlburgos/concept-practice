

def draw_spiral_of_size_n(n):
    block = make_block(n)

    r = 0
    c = 0
    max_marks = n

    while max_marks > 0:

        for i in range(max_marks):
            block[r][c] = 'x'
            # prevents taking c out of the range of the columns and moves to the
            # next row
            if i < max_marks - 1:
                c += 1
            else:
                r += 1

        max_marks -= 1

        for i in range(max_marks):
            block[r][c] = 'x'
            if i < max_marks - 1:
                r += 1
            else:
                c -=1

        max_marks -= 1

        for i in range(max_marks):
            block[r][c] = 'x'
            if i < max_marks - 1:
                c -= 1
            else:
                r -= 1

        max_marks -= 1

        for i in range(max_marks):
            block[r][c] = 'x'
            if i == max_marks - 1:
                c += 1
            else:
                r -= 1

        max_marks -= 1

    print_chars(block)



################################################################################
################################################################################
# Helpers

def print_block(block):
    for row in block:
        print row

    print '*'*60


def print_chars(block):
    for row in block:
        # for col in row:
        #     print col,
        # print '\n'
        for i in range(len(row)):
            if i == len(row) - 1:
                print row[i]
            else:
                print row[i],

    # print '*'*60


def make_block(n):
    row = [' ']*n

    block = []

    for i in range(n):
        new_row = list(row)
        block.append(new_row)

    return block

# # This is broken because all rows point to the same array
# def broken_make_block(n):
#     row = ['']*n

#     block = []

#     for i in range(n):
#         block.append(row)

#     return block

################################################################################
################################################################################

# !!!!!!!!!!
# I dont like this version because it drops the last x from the spiral 
def v2_draw_spiral_of_size_n(n):
    block = make_block(n)

    # print_block(block)

    r = 0
    c = 0
    max_marks = n - 1

    while max_marks > 0:

        print 'leg_len:', max_marks

        for i in range(max_marks):
            block[r][c] = 'x'
            c += 1
            # print_chars(block)

        # print_block(block)
        max_marks -= 1

        print 'leg_len:', max_marks

        for i in range(max_marks):
            block[r][c] = 'x'
            r += 1

        # print_block(block)

        max_marks -= 1

        print 'leg_len:', max_marks

        for i in range(max_marks):
            block[r][c] = 'x'
            c -= 1

        # print_block(block)

        max_marks -= 1
        
        print 'leg_len:', max_marks

        for i in range(max_marks):
            block[r][c] = 'x'
            r -= 1

        # print_block(block)
        max_marks -= 1
        print 'leg_len:', max_marks

    print_chars(block)


def draw_an_X_rec(n):
    block = make_block(n)

    x = _draw_an_x(block, l=0, r=n-1)

    print_chars(x)


def _draw_an_x(block, l, r):
    if l > r:
        return block

    block[l][l] = 'x'
    block[l][r] = 'x'
    block[r][l] = 'x'
    block[r][r] = 'x'

    return _draw_an_x(block, l=l+1, r=r-1)


def rec_draw_a_spiral(n):
    block = make_block(n)

    spiral = _draw_a_spiral(block=block, leg_len=n, r=0, c=0, direction='R')

    print_chars(spiral)

def _draw_a_spiral(block, leg_len, r, c, direction):
    if leg_len == 0:
        return block

    if direction == 'R':
        for i in range(leg_len):
            block[r][c + i] = 'x'
        return _draw_a_spiral(block,
                              leg_len=leg_len - 1,
                              r=r+1,
                              c=c+leg_len-1,
                              direction='D')
    elif direction == 'D':
        for i in range(leg_len):
            block[r + i][c] = 'x'
        return _draw_a_spiral(block,
                              leg_len=leg_len - 1,
                              r=r+leg_len-1,
                              c=c-1,
                              direction='L')

    elif direction == 'L':
        for i in range(leg_len):
            block[r][c - i] = 'x'
        return _draw_a_spiral(block,
                              leg_len=leg_len - 1,
                              r=r - 1,
                              c=c - (leg_len - 1),
                              direction='U')

    elif direction == 'U':
        for i in range(leg_len):
            block[r - i][c] = 'x'
        return _draw_a_spiral(block,
                              leg_len=leg_len - 1,
                              r=r - (leg_len - 1),
                              c=c + 1,
                              direction='R')


def rec_draw_a_spiral_v2(n):
    block = make_block(n)

    spiral = _draw_a_spiral_v2(block=block, leg_len=n, r=0, c=0, pass_num=0)

    print_chars(spiral)


def _draw_a_spiral_v2(block, leg_len, r, c, pass_num):
    if leg_len == 0:
        return block

    control = {'0': {'row_inc': 0,
                     'col_inc': 1,
                     'row_adj': 1,
                     'col_adj': leg_len - 1,
                     },
               '1': {'row_inc': 1,
                     'col_inc': 0,
                     'row_adj': leg_len - 1,
                     'col_adj': -1,
                     },
               '2': {'row_inc': 0,
                     'col_inc': -1,
                     'row_adj': -1,
                     'col_adj': -(leg_len - 1),
                     },
               '3': {'row_inc': -1,
                     'col_inc': 0,
                     'row_adj': -(leg_len - 1),
                     'col_adj': 1,
                     },
               }

    control_key = str(pass_num % 4)

    controler = control[control_key]

    # print 'leg_len:', leg_len
    for i in range(leg_len):
        row = r + i*controler['row_inc']
        col = c + i*controler['col_inc']
        # print 'row, col:', row, col
        block[row][col] = 'x'

    return _draw_a_spiral_v2(block=block,
                             leg_len=leg_len - 1,
                             r=r + controler['row_adj'],
                             c=c + controler['col_adj'],
                             pass_num=pass_num + 1,
                             )

