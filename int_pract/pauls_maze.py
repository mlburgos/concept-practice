
def path(maze):

    # ~~~~~~ Don't fall into the trap of manually taking the first step.
    # ~~~~~~ Let the recursion do the work.
    # path1 = _path(x=0, y=1, ((0,0), (0,1)))
    # path2 = _path(x=1, y=0, ((0,0), (1,0)))

    # if path1:
    #     return [D] + path1
    # elif path2:
    #     return [R] + path2

    # return None

    visited = set()
    visited.add((0, 0))

    return _path(x=0, y=0, visited=visited, maze=maze)


def _path(x, y, visited, maze):
    # x = column position
    # y = rows

    print 'visited:', visited
    print 'maze[y][x]:', maze[y][x]

    if maze[y][x] == 'x':
        return []
    if maze[y][x] == '.':
        return None

    if (x - 1 >= 0) and ((x - 1, y) not in visited):
        visited.add((x - 1, y))
        path = _path(x - 1, y, visited, maze)

        if path is not None:
            return ['L'] + path

    if (x + 1 < len(maze[0])) and ((x + 1, y) not in visited):
        visited.add((x + 1, y))
        path = _path(x + 1, y, visited, maze)

        if path is not None:
            return ['R'] + path

    if (y - 1 >= 0) and ((x, y - 1) not in visited):
        visited.add((x, y - 1))
        path = _path(x, y - 1, visited, maze)

        if path is not None:
            return ['U'] + path

    if (x + 1 < len(maze)) and ((x, y + 1) not in visited):
        visited.add((x, y + 1))
        path = _path(x, y + 1, visited, maze)

        if path is not None:
            return ['D'] + path

    return None


maze1 = [[0, '.', 0],
         [0, 0, 0],
         ['.', '.', 'x'],
         ]

