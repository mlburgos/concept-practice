# Write a function to check that a binary tree ↴ is a valid binary search tree ↴ .

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right



def is_valid_binary_tree(root):

    # each tuple in the stack will be of the form:
    # (node, upper_bound, lower_bound)
    stack = [(root, None, None)]

    # ***** come back and check this condition *****
    while stack:
        node, upper_bound, lower_bound = stack.pop()

        # test if current node violates bounds
        if upper_bound is not None and node.data >= upper_bound:
            return False
        
        if lower_bound is not None and node.data <= lower_bound:
            return False

        # if not, add its children to the stack
        if node.right:
            stack.append((node.right, upper_bound, node.data))
        if node.left:
            stack.append((node.left, node.data, lower_bound))

    return True

