class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node{}'.format(self.data)


class LL(object):

    def __init__(self, head):
        self.head = head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1

l_l1 = LL(node1)


def has_cycle(head):
    past_nodes = set()
    current = head

    while current:
        past_nodes.add(current)
        if current.next in past_nodes:
            return True
        current = current.next

    return False
