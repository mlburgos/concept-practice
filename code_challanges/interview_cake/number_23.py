# You have a singly-linked list ↴ and want to check if it contains a cycle.

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
# e.next = d


# O(n) time, O(n) space

def is_a_cycle(node):
    visited = set([node])

    current = node

    while current is not None:
        if current.next is None:
            return False

        if current.next in visited:
            return True

        if current.next and current.next not in visited:
            visited.add(current.next)
            current = current.next


# Interview Cake solution
# slow_runner and fast_runner

def is_cyclical(node):

    slow_runner = node
    fast_runner = node

    i = 1
    while True:

        if fast_runner is None:
            return False

        fast_runner = fast_runner.next

        if fast_runner == slow_runner:
            print 'slow_runner:', slow_runner
            print 'fast_runner:', fast_runner

            return True

        if i % 2 == 0:
            slow_runner = slow_runner.next

        print 'slow_runner:', slow_runner
        print 'fast_runner:', fast_runner
        print '-'*20

        i += 1
    





