my_rectangle1 = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,

}

# overlaps with my_rectangle1
# {'bottom_y': 5, 'height': 2, 'left_x': 5, 'width': 6}
my_rectangle2 = {

    # coordinates of bottom-left corner
    'left_x': 5,
    'bottom_y': 3,

    # width and height
    'width': 10,
    'height': 4,

}

# no overlap with my_rectangle1
my_rectangle3 = {

    # coordinates of bottom-left corner
    'left_x': 15,
    'bottom_y': 3,

    # width and height
    'width': 10,
    'height': 4,

}

# contains my_rectangle1, therefore return my_rectangle1
# {'bottom_y': 5, 'height': 4, 'left_x': 1, 'width': 10}
my_rectangle4 = {

    # coordinates of bottom-left corner
    'left_x': 0,
    'bottom_y': 0,

    # width and height
    'width': 20,
    'height': 20,

}

# this rectangle doesn't intersect my_rectangle1, but it does share an edge
# returns the edge (has width = 0)
# {'bottom_y': 5, 'height': 4, 'left_x': 11, 'width': 0}
my_rectangle5 = {

    # coordinates of bottom-left corner
    'left_x': 11,
    'bottom_y': 0,

    # width and height
    'width': 20,
    'height': 20,

}

def find_intersecting_rect(rect1, rect2):

    x_range_1 = (rect1['left_x'], rect1['left_x'] + rect1['width'])
    y_range_1 = (rect1['bottom_y'], rect1['bottom_y'] + rect1['height'])

    x_range_2 = (rect2['left_x'], rect2['left_x'] + rect2['width'])
    y_range_2 = (rect2['bottom_y'], rect2['bottom_y'] + rect2['height'])

    if x_range_2[0] in xrange(x_range_1[0], x_range_1[1] + 1):
        mini = x_range_2[0]
    elif x_range_1[0] in xrange(x_range_2[0], x_range_2[1] + 1):
        mini = x_range_1[0]
    else:
        return 'No overlap'

    if x_range_2[1] in xrange(x_range_1[0], x_range_1[1] + 1):
        maxi = x_range_2[1]
    elif x_range_1[1] in xrange(x_range_2[0], x_range_2[1] + 1):
        maxi = x_range_1[1]
    else:
        return 'No overlap'

    x_range_overlap = (mini, maxi)
    print 'x_range_overlap:', x_range_overlap

    if y_range_2[0] in xrange(y_range_1[0], y_range_1[1] + 1):
        mini = y_range_2[0]
    elif y_range_1[0] in xrange(y_range_2[0], y_range_2[1] + 1):
        mini = y_range_1[0]
    else:
        return 'No overlap'

    if y_range_2[1] in xrange(y_range_1[0], y_range_1[1] + 1):
        maxi = y_range_2[1]
    elif y_range_1[1] in xrange(y_range_2[0], y_range_2[1] + 1):
        maxi = y_range_1[1]
    else:
        return 'No overlap'

    y_range_overlap = (mini, maxi)
    print 'y_range_overlap:', y_range_overlap

    overlarping_rect = {
        # coordinates of bottom-left corner
        'left_x': x_range_overlap[0],
        'bottom_y': y_range_overlap[0],

        # width and height
        'width': x_range_overlap[1] - x_range_overlap[0],
        'height': y_range_overlap[1] - y_range_overlap[0],
    }

    return overlarping_rect

################################################################################

def get_min_and_max_of_overlap(range1, range2):

    if range2[0] in xrange(range1[0], range1[1] + 1):
        mini = range2[0]
    elif range1[0] in xrange(range2[0], range2[1] + 1):
        mini = range1[0]
    else:
        return None

    if range2[1] in xrange(range1[0], range1[1] + 1):
        maxi = range2[1]
    elif range1[1] in xrange(range2[0], range2[1] + 1):
        maxi = range1[1]
    else:
        return None

    return (mini, maxi)


def find_intersecting_rect(rect1, rect2):

    x_range_1 = (rect1['left_x'], rect1['left_x'] + rect1['width'])
    y_range_1 = (rect1['bottom_y'], rect1['bottom_y'] + rect1['height'])

    x_range_2 = (rect2['left_x'], rect2['left_x'] + rect2['width'])
    y_range_2 = (rect2['bottom_y'], rect2['bottom_y'] + rect2['height'])

    x_range_overlap = get_min_and_max_of_overlap(x_range_1, x_range_2)
    print 'x_range_overlap:', x_range_overlap

    if x_range_overlap is None:
        return None

    y_range_overlap = get_min_and_max_of_overlap(y_range_1, y_range_2)
    print 'y_range_overlap:', y_range_overlap

    if y_range_overlap is None:
        return None

    overlarping_rect = {
        # coordinates of bottom-left corner
        'left_x': x_range_overlap[0],
        'bottom_y': y_range_overlap[0],

        # width and height
        'width': x_range_overlap[1] - x_range_overlap[0],
        'height': y_range_overlap[1] - y_range_overlap[0],
    }

    return overlarping_rect
