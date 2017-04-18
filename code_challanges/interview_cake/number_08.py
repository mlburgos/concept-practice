# Write a function to see if a binary tree ↴ is "superbalanced" (a new tree
# property we just made up).
# A tree is "superbalanced" if the difference between the depths of any two
# leaf nodes ↴ is no greater than one.


class BinaryTreeNode(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Tree B; should pass
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


# Tree A; should not pass
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
node6_a.left = node5_a
node6_a.right = node7_a
node12_a.left = node10_a
node12_a.right = node14_a
node10_a.left = node9_a
node10_a.right = node11_a
node14_a.left = node13_a
node14_a.right = node15_a
node15_a.right = node17_a

# C should fail
node1_c = BinaryTreeNode(1)
node2_c = BinaryTreeNode(2)
node3_c = BinaryTreeNode(3)

node1_c.right = node2_c
node2_c.right = node3_c

# attempt 1: doesn't work because it could end up with varying values
def is_superbalanced(root_node):
    return not not _is_superbalanced(root_node)


def _is_superbalanced(node):

    if node is None:
        return 0

    depth_left = _is_superbalanced(node.left)
    depth_right = _is_superbalanced(node.right)

    if not depth_left or not depth_right:
        return False

    if abs(depth_left - depth_right) > 1:
        return False

    return max(depth_left, depth_right) + 1


# attempt 2: recursive solution that does work, but they want an iterative
# solution...
def is_superbalanced(root_node):
    result = _is_superbalanced(root_node)
    return result[0]


def _is_superbalanced(node):
    if node is None:
        return [True, 0, 0]

    # print node.data

    left_bool, left_min, left_max = _is_superbalanced(node.left)
    right_bool, right_min, right_max = _is_superbalanced(node.right)

    # print 'node.data [left_bool, left_min, left_max]:', node.data, left_bool, left_min, left_max
    # print 'node.data [right_bool, right_min, right_max]:', node.data, right_bool, right_min, right_max

    if not left_bool or not right_bool:
        return [False, 0, 0]

    mini = min(left_min, right_min)
    maxi = max(left_max, right_max)

    if maxi - mini > 1:
        return [False, 0, 0]

    return [True, mini + 1, maxi + 1]


# attempt 3: iteratively
def is_superbal(node):

    current = node
    maxi = None
    mini = None

    stack = []
    count = 0

    while current:

        if current == 'pop':
            count -= 1
            current = stack.pop()
            print 'pop!'
            print 'count:', count
            continue
        
        count += 1
        print 'current.data:', current.data
        print 'count:', count

        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)

        print 'stack:', stack

        if current.left is None and current.right is None:
            if maxi is None:
                maxi = count
            else:
                maxi = max(maxi, count)
            if mini is None:
                mini = count
            else:
                mini = min(mini, count)

            print 'mini:', mini
            print 'maxi:', maxi

            if stack:
                current = stack.pop()
            else:
                break

            print 'stack:', stack
            continue

        if stack:
            current = stack.pop()
            stack.append('pop')
        else:
            break

        print 'stack:', stack

    return maxi - mini <= 1



# attempt 3, round 2: iteratively
def is_superbal(node):

    current = node
    maxi = None
    mini = None

    stack = []
    count = 1
    prior_side = None

    while current:

        if current == 'R':
            current = stack.pop()
            continue
        if current == 'L':
            reduce_count_by_extra_1 = True
            current = stack.pop()
            continue

        # if we've hit a leaf node:
        if current.left is None and current.right is None:
            if maxi is None:
                maxi = count
            else:
                maxi = max(maxi, count)
            if mini is None:
                mini = count
            else:
                mini = min(mini, count)

            if stack:
                current = stack.pop()
            else:
                break

            # if the leaf is a left node, reduce the count
            if reduce_count_by_extra_1:
                count -= 1

            continue

        # add children to stack if not a leaf node
        if current.left is not None:
            stack.append(current.left)
            stack.append('L')
        if current.right is not None:
            stack.append(current.right)
            stack.append('R')

        # move to the next node in the stack
        if stack:
            current = stack.pop()
        else:
            break

        count += 1


    return maxi - mini <= 1

#############    #################################################################
# applying the interview cake method from mem/head

def is_superbal(root_node):

    if root_node is None:
        return True

    depths = []

    # nodes will be a list of nodes and their respective depths
    nodes = []
    nodes.append((root_node, 0))

    while len(nodes):
        node, depth = nodes.pop()
        print 'node:', node
        print 'depth:', depth

        # if the node is a leaf (i.e. has no children):
        if not node.left and not node.right:

            if depth not in depths:
                depths.append(depth)

            if len(depths) > 2 or max(depths) - min(depths) > 1:
                print 'depths:', depths
                return False

        if node.left:
            nodes.append((node.left, depth + 1))
        if node.right:
            nodes.append((node.right, depth + 1))

    return True


#################################################################################
# their exact solution

def is_balanced(tree_root):

    # a tree with no nodes is superbalanced, since there are no leaves!
    if tree_root == None:
        return True

    depths = [] # we short-circuit as soon as we find more than 2

    # we'll treat this list as a stack that will store tuples of (node, depth)
    nodes = []
    nodes.append((tree_root, 0))

    while len(nodes):

        # pop a node and its depth from the top of our stack
        node, depth = nodes.pop()

        # case: we found a leaf
        if (not node.left) and (not node.right):

            # we only care if it's a new depth
            if depth not in depths:
                depths.append(depth)

                # two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart
                if (len(depths) > 2) or \
                        (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False

        # case: this isn't a leaf - keep stepping down
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    if len(depths) == 1:
        return False

    return True