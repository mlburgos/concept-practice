# reverse a linked list


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

l_l1 = LL(node1)


def traverse(head):

    current = head
    while current:
        print current.data

        current = current.next


def reverse(head):

    current = head.next
    first = head
    previous = head

    while current:
        temp = current
        current = previous.next.next
        previous.next = current
        temp.next = first
        first = temp

    traverse(first)
