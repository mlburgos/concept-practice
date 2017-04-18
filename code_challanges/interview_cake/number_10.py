# find 2nd largest number in a binary tree


class BinaryTreeNode(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

node1_b = BinaryTreeNode(1)
node2_b = BinaryTreeNode(2)
node3_b = BinaryTreeNode(3)
node4_b = BinaryTreeNode(4)
node5_b = BinaryTreeNode(5)
node6_b = BinaryTreeNode(6)
node7_b = BinaryTreeNode(7)
node8_b = BinaryTreeNode(8)
node9_b = BinaryTreeNode(9)
node10_b = BinaryTreeNode(10)
node11_b = BinaryTreeNode(11)
node12_b = BinaryTreeNode(12)
node13_b = BinaryTreeNode(13)
node14_b = BinaryTreeNode(14)
node15_b = BinaryTreeNode(15)
node16_b = BinaryTreeNode(16)
node17_b = BinaryTreeNode(17)


node8_b.left = node4_b
node8_b.right = node12_b
node4_b.left = node2_b
node4_b.right = node6_b
node2_b.left = node1_b
node2_b.right = node3_b
node6_b.left = node5_b
node6_b.right = node7_b
node12_b.left = node10_b
node12_b.right = node14_b
node10_b.left = node9_b
node10_b.right = node11_b
node14_b.left = node13_b
node14_b.right = node15_b


node1_a = BinaryTreeNode(1)
node2_a = BinaryTreeNode(2)
node3_a = BinaryTreeNode(3)
node4_a = BinaryTreeNode(4)
node5_a = BinaryTreeNode(5)
node6_a = BinaryTreeNode(6)
node7_a = BinaryTreeNode(7)
node8_a = BinaryTreeNode(8)
node9_a = BinaryTreeNode(9)
node10_a = BinaryTreeNode(10)
node11_a = BinaryTreeNode(11)
node12_a = BinaryTreeNode(12)
node13_a = BinaryTreeNode(13)
node14_a = BinaryTreeNode(14)
node15_a = BinaryTreeNode(15)
node16_a = BinaryTreeNode(16)
node17_a = BinaryTreeNode(17)


node8_a.left = node4_a
node8_a.right = node12_a
node4_a.left = node2_a
node4_a.right = node6_a
node2_a.left = node1_a
node2_a.right = node3_a
node6_a.left = node5_a
node6_a.right = node7_a
node12_a.left = node10_a
node12_a.right = node14_a
node10_a.left = node9_a
node10_a.right = node11_a
node14_a.left = node13_a
node14_a.right = node17_a
node17_a.left = node15_a


node1_c = BinaryTreeNode(1)
node2_c = BinaryTreeNode(2)
node3_c = BinaryTreeNode(3)
node4_c = BinaryTreeNode(4)
node5_c = BinaryTreeNode(5)
node6_c = BinaryTreeNode(6)
node7_c = BinaryTreeNode(7)
node8_c = BinaryTreeNode(8)
node9_c = BinaryTreeNode(9)
node10_c = BinaryTreeNode(10)
node11_c = BinaryTreeNode(11)
node12_c = BinaryTreeNode(12)
node13_c = BinaryTreeNode(13)
node14_c = BinaryTreeNode(14)
node15_c = BinaryTreeNode(15)
node16_c = BinaryTreeNode(16)
node17_c = BinaryTreeNode(17)

# should return 11
node8_c.left = node4_c
node8_c.right = node12_c
node4_c.left = node2_c
node4_c.right = node6_c
node2_c.left = node1_c
node2_c.right = node3_c
node6_c.left = node5_c
node6_c.right = node7_c
node12_c.left = node10_c
node10_c.left = node9_c
node10_c.right = node11_c


################################################################################
# Attempt 1: works, but they want it faster and smaller (wrt space in memory)
# O(n) time and O(h) space, where h = height (which is lg(n) if the BST is
# balanced)

def find_second_largest(node):

    largest = node.data
    second_largest = None

    # dfs
    stack = [node]

    while stack:
        current = stack.pop()

        if current.data > largest:
            second_largest = largest
            largest = current.data
        elif second_largest is None or current.data > second_largest:
            second_largest = current.data

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return second_largest


################################################################################
# Attempt 2: First try at beating O(n) runtime and O(height) runspace
# ... this is an improvement on speed O(n/2), but still O(n)

def find_second_largest(node):
    if node.right is None:
        if node.left:
            return node.left.data
        return None

    largest = node.right.data
    second_largest = node.data

    stack = [node.right]

    while stack:
        current = stack.pop()

        if current.data > largest:
            second_largest = largest
            largest = current.data
        elif second_largest is None or current.data > second_largest:
            second_largest = current.data

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return second_largest


################################################################################
# Attempt 3: Second try at beating O(n) runtime and O(height) runspace
# O(h) runtime and O(1) space!

def find_largest(node):
    # return the right-most node in the tree

    current = node

    while current.right:
        current = current.right

    return current


def find_second_largest(node):

    current = node
    parent = None

    while True:

        if current.right is None:
            if current.left:
                second_largest = find_largest(current.left)
                return second_largest
            else:
                return parent

        parent = current
        current = current.right




