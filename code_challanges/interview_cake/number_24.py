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
# c.next = d
# d.next = e


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


def traverse(node):
    current = node
    while current:
        print current
        current = current.next



# Interview cake version

def rev_ll(head):
    current = head
    previous = None
    next = None

    while current:
        next = current.next
        print 'next:', next

        # Since previous starts out as None, just always set current.next to
        # previous instead of writing out an explicit case for that
        #
        # if previous:
        #     current.next = previous
        # else:
        #     current.next = None

        current.next = previous

        previous = current
        print 'previous:', previous
        current = next
        print 'current:', current


