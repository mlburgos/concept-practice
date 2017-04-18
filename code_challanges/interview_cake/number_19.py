
# Implement a queue ↴ with 2 stacks ↴ . Your queue should have an enqueue and a
# dequeue function and it should be "first in first out" (FIFO).
# Optimize for the time cost of mm function calls on your queue. These can be
# any mix of enqueue and dequeue calls.
# 
# Assume you already have a stack implementation and it gives O(1) time push
# and pop.

################################################################################
# Attempt 1: too slow for Parker

class My_Queue(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, item):
        self.stack_1.append(item)

    def dequeue(self):
        if len(self.stack_1) == 0:
            return 'Queue is empty'

        while self.stack_1:
            item = self.stack_1.pop()
            self.stack_2.append(item)

        return_item = self.stack_2.pop()

        while self.stack_2:
            item = self.stack_2.pop()
            self.stack_1.append(item)

        return return_item

################################################################################
# Attempt 2: don't put everything back onto stack_1
#
# in:  [1,2,3,4,5]
# out: []
#
# dequeue
#
# in:  []
# out: [5,4,3,2]
#
# enqueue(6)
#
# in:  [6]
# out: [5,4,3,2]
#
# dequeue
#
# in: [6]
# out: [5,4,3]
#
# enqueue(7)
#
# in: [6,7]
# out: [5,4,3]


class My_Q(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if self.out_stack:
            return self.out_stack.pop()

        while self.in_stack:
            item = self.in_stack.pop()
            self.out_stack.append(item)

        return self.out_stack.pop()










































