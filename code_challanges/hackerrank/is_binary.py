# Given a root node, determine whether or not it is a binary tree

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Tree(object):

    def __init__(self, root):
        self.root = root


class BinaryTreeNode(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Tree B is not correct
node6_b = BinaryTreeNode(6)
node4_b = BinaryTreeNode(4)
node8_b = BinaryTreeNode(8)
node3_b = BinaryTreeNode(3)
node5_b = BinaryTreeNode(5)
node7_b = BinaryTreeNode(7)
node9_b = BinaryTreeNode(9)

node6_b.left = node4_b
node6_b.right = node8_b
node4_b.left = node3_b
node4_b.right = node7_b
node8_b.right = node9_b

# Tree C is a bigger version of Tree A; also should pass
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


node8_c.left = node4_c
node8_c.right = node12_c
node4_c.left = node2_c
node4_c.right = node6_c
node2_c.left = node1_c
node2_c.right = node3_c
node6_c.left = node5_c
node6_c.right = node7_c
node12_c.left = node10_c
node12_c.right = node14_c
node10_c.left = node9_c
node10_c.right = node11_c
node14_c.left = node13_c
node14_c.right = node15_c

# Tree D should fail

node1_d = BinaryTreeNode(1)
node2_d = BinaryTreeNode(2)
node3_d = BinaryTreeNode(3)
node4_d = BinaryTreeNode(4)
node5_d = BinaryTreeNode(5)
node6_d = BinaryTreeNode(6)
node7_d = BinaryTreeNode(7)
node8_d = BinaryTreeNode(8)
node9_d = BinaryTreeNode(9)
node10_d = BinaryTreeNode(10)
node11_d = BinaryTreeNode(11)
node12_d = BinaryTreeNode(12)
node13_d = BinaryTreeNode(13)
node14_d = BinaryTreeNode(14)
node15_d = BinaryTreeNode(15)
node16_d = BinaryTreeNode(16)
node17_d = BinaryTreeNode(17)

node8_d.left = node4_d
node8_d.right = node12_d
node4_d.left = node2_d
node4_d.right = node6_d
node2_d.left = node1_d
node2_d.right = node3_d
node6_d.left = node5_d
# node6_d.right should cause this to fail
node6_d.right = node16_d
node12_d.left = node10_d
node12_d.right = node14_d
node10_d.left = node9_d
node10_d.right = node11_d
node14_d.left = node13_d
node14_d.right = node15_d


# Tree E should fail

node0_e = BinaryTreeNode(0)
node1_e = BinaryTreeNode(1)
node2_e = BinaryTreeNode(2)
node3_e = BinaryTreeNode(3)
node4_e = BinaryTreeNode(4)
node5_e = BinaryTreeNode(5)
node6_e = BinaryTreeNode(6)
node7_e = BinaryTreeNode(7)
node8_e = BinaryTreeNode(8)
node9_e = BinaryTreeNode(9)
node10_e = BinaryTreeNode(10)
node11_e = BinaryTreeNode(11)
node12_e = BinaryTreeNode(12)
node13_e = BinaryTreeNode(13)
node14_e = BinaryTreeNode(14)
node15_e = BinaryTreeNode(15)
node16_e = BinaryTreeNode(16)
node17_e = BinaryTreeNode(17)

node8_e.left = node4_e
node8_e.right = node12_e
node4_e.left = node2_e
node4_e.right = node6_e
node2_e.left = node1_e
node2_e.right = node3_e
node6_e.left = node5_e
node6_e.right = node7_e
node12_e.left = node10_e
node12_e.right = node14_e
node10_e.left = node9_e
node10_e.right = node11_e
# node14_e.leftt should cause this to fail
node14_e.left = node0_e
node14_e.right = node15_e


# Tree A is a binary search tree
node6_a = BinaryTreeNode(6)
node4_a = BinaryTreeNode(4)
node8_a = BinaryTreeNode(8)
node3_a = BinaryTreeNode(3)
node5_a = BinaryTreeNode(5)
node7_a = BinaryTreeNode(7)
node9_a = BinaryTreeNode(9)

node6_a.left = node4_a
node6_a.right = node8_a
node4_a.left = node3_a
node4_a.right = node5_a
node8_a.left = node7_a
node8_a.right = node9_a

###########################################################################


def is_binary(root):
    return (_is_binary(node=root.left, mini=None, maxi=root.data) and
            _is_binary(node=root.right, mini=root.data, maxi=None))


def _is_binary(node, mini, maxi):
    if node is None:
        return True

    if mini and node.data <= mini:
        return False

    if maxi and node.data >= maxi:
        return False

    return (_is_binary(node=node.left, mini=mini, maxi=node.data) and
            _is_binary(node=node.right, mini=node.data, maxi=maxi))


###########################################################################
# Failed attempt

# def is_binary(node, parent=None):
#     # Base case
#     if node is None:
#         return True

#     left = node.left
#     right = node.right

#     # General rule. Left child must be less, right must be greater
#     if ((left is not None and
#             left.data >= node.data) or
#         (right is not None and
#             right.data <= node.data)
#         ):
#         print "Broke general rule at node:", node.data
#         return False

#     if parent is not None:
#         if (node.data < parent.data and
#                 right is not None and
#                 right.data >= parent.data):
#             print "Right >= parent at node:", node.data
#             return False

#         if (node.data > parent.data and
#                 left is not None and
#                 left.data <= parent.data):
#             print "Left <= parent at node:", node.data
#             return False

#     return (is_binary(left, node) and
#             is_binary(right, node))


###########################################################################

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


# def check_binary_search_tree_(root):
#     return (check_child(mini=None, maxi=root.data, node=root.left) and
#             check_child(mini=root.data, maxi=None, node=root.right))


# def check_child(mini, maxi, node):
#     if node is None:
#         return True
#     if mini:
#         if node.data <= mini:
#             return False
#     if maxi:
#         if node.data >= maxi:
#             return False
#     return (check_child(mini, node.data, node.left) and
#             check_child(node.data, maxi, node.right))

###########################################################################

# def check_binary_search_tree_(root):
#     return (is_binary(mini=None, maxi=root , current=root.left) and
#             is_binary(mini=root, maxi=None , current=root.right))

# def is_binary(mini, maxi, current):
#     if current is None:
#         return True
    
#     if maxi:
#         if current.data >= maxi:
#             return False
    
#     if mini:
#         if current.data <= mini:
#             return False
    
#     return (is_binary(mini=mini, maxi=current , current=current.left) and
#             is_binary(mini=current, maxi=maxi , current=current.right))





