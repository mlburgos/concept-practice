depth_first_search.py


class Node(object):

    def __init__(self, data):
        self.data = data
        self.childern = []

node1_a = Node(1)
node2_a = Node(2)
node3_a = Node(3)
node4_a = Node(4)
node5_a = Node(5)
node6_a = Node(6)
node7_a = Node(7)
node8_a = Node(8)
node9_a = Node(9)
node10_a = Node(10)
node11_a = Node(11)
node12_a = Node(12)
node13_a = Node(13)
node14_a = Node(14)
node15_a = Node(15)
node16_a = Node(16)
node17_a = Node(17)
 

node1_a.childern = [node2_a, node3_a, node4_a]

node2_a.childern = [node5_a, node6_a, node7_a]

node3_a.childern = [node8_a, node9_a]

node4_a.childern = [node10_a, node11_a, node12_a]

node12_a.childern = [node13_a, node14_a]


