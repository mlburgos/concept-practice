from random import randint


# class Stack:

#     # initialize an empty list
#     def __init__(self):
#         self.items = []
#         self.maxes = [None]

#     # push a new item to the last index
#     def push(self, item):
#         current_max = self.maxes[-1]

#         if current_max is None or current_max < item:
#             current_max = item

#         self.maxes.append(current_max)
#         self.items.append(item)

#     # remove the last item
#     def pop(self):
#         # if the stack is empty, return None
#         # (it would also be reasonable to throw an exception)
#         if not self.items:
#             return None

#         self.maxes.pop()
#         return self.items.pop()

#     # see what the last item is
#     def peek(self):
#         if not self.items:
#             return None
#         return self.items[-1]

#     def get_max(self):
#         return self.maxes[-1]

#     def show_data(self):
#         print 'self.items:', self.items
#         print 'self.maxes:', self.maxes



# s = Stack()

# for i in xrange(10):
#     s.push(randint(0, 100))



################################################################################
# the first one worked, but using inheritance...


class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class MaxStack:

    def __init__(self):
        self.items = Stack()
        self.maxes = Stack()

    def push(self, item):
        maxi = self.maxes.peek()

        if item > maxi:
            maxi = item

        self.maxes.push(maxi)
        self.items.push(item)

    def pop(self):
        self.items.pop()
        self.maxes.pop()

    def peek(self):
        self.items.peek()

    def get_max(self):
        self.maxes.peek()

    def show_data(self):
        print 'self.items.items:', self.items.items
        print 'self.maxes.items:', self.maxes.items


m = MaxStack()

for i in xrange(10):
    m.push(randint(0, 100))

