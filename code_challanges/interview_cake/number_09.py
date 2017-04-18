# recursive solution:


def is_binary(root_node):
    return _is_binary(node=root_node, mini=None, maxi=None)


def _is_binary(node, mini, maxi):
    if node is None:
        return True

    if mini and node.data <= mini:
        return False

    if maxi and node.data >= maxi:
        return False

    return all(_is_binary(node.left, mini=mini, maxi=node.data),
               _is_binary(node.right, mini=node.data, maxi=maxi))


# itterative solution:

def is_binanry(root_node):
    # dfs
    stack = [(root_node, None, None)]

    while stack:
        node, maxi, mini = stack.pop()

        if maxi and node.data >= maxi:
            return False
        if mini and node.data <= mini:
            return False

        if node.left:
            # left: maxi = current node.data; mini = mini
            stack.append((node.left, node.data, mini))

        if node.right:
            # right: maxi = maxi; mini = current node.data
            stack.append((node.right, maxi, node.data))

    return True

