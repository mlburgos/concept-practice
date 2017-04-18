# print statements for error checking
#         print "start of pop- first:", self.first
#         print "start of pop- second:", self.second

#                 print "1st for- self.first:", self.first
#                 print "1st for- self.second:", self.second

#             print "btwn- retval:", retval
#             print "btwn- self.first:", self.first
#             print "btwn- self.second:", self.second


class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if self.first:
            for i in range(len(self.first)):
                self.second.append(self.first.pop())

            retval = self.second.pop()

            self.first.append(retval)

            for i in range(len(self.second)):
                self.first.append(self.second.pop())

            return retval

        else:
            return None

    def pop(self):
        if self.first:
            for i in range(len(self.first)):
                self.second.append(self.first.pop())

            retval = self.second.pop()

            for i in range(len(self.second)):
                self.first.append(self.second.pop())

            return retval

        else:
            return None

    def put(self, value):
        self.first.append(value)


queue = MyQueue()

# t = int(raw_input())
# for line in xrange(t):
#     values = map(int, raw_input().split())

#     if values[0] == 1:
#         queue.put(values[1])
#     elif values[0] == 2:
#         queue.pop()
#     else:
#         print queue.peek()

pairs = [(1, 42),
         (2,),
         (1, 14),
         (3,),
         (2, 28),
         (3,),
         (1, 60),
         (1, 78),
         (2,),
         (2,)
         ]


# for values in pairs:

#     if values[0] == 1:
#         queue.put(values[1])
#     elif values[0] == 2:
#         queue.pop()
#     else:
#         print queue.peek()

