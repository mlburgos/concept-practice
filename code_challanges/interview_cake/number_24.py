# Write a function for reversing a linked list. Do it in-place .

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

    def __repr__(self):
        return 'Node {}'.format(self.value)

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')
e = LinkedListNode('E')

a.next = b
b.next = c
c.next = d
d.next = e


def reverse_LL(head):
    if head.next:
        current = head.next
    else:
        raise Exeption('Need more than one node.')

    new_head = head
    end = head

    while current and current != end:
        print 'new_head:', new_head
        end.next = current.next
        current.next = new_head
        new_head = current
        current = end.next

    return new_head
