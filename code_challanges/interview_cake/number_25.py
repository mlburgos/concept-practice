# You have a linked list ↴ and want to find the kkth to last node.


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return 'Node Data: {}'.format(self.value)


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# kth_to_last_node(2, a)
# returns the node with value "Devil's Food" (the 2nd to last node)

# First attempt
# O(n) time O(n) space

def kth_to_last_node(k, head):

    node_list = []

    current = head

    while current:
        node_list.append(current)
        current = current.next

    i = len(node_list) - k

    return node_list[i] if(i >= 0) else None
    # return i >= 0 ? node_list[i] : None

################################################################################
# Second attempt
# Aiming for O(n) time and O(1) space


def kth_to_last_node(k, head):
    current = head
    len_of_ll = 0

    while current:
        len_of_ll += 1
        current = current.next

    current = head
    looking_for = len_of_ll - k
    if looking_for < 0:
        raise Exception('List too short for desired k')

    i = 0

    while current:
        if i == looking_for:
            return current

        i += 1
        current = current.next

