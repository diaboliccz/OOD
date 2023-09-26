class Node:
    order = 0
    def __init__(self, data):
        self.data = [Node.order, data]
        self.left = None
        self.right = None
        Node.order += 1
    
    def __str__(self):
        return str(self.data)

Node1 = Node(5)
Node2 = Node(4)
Node3 = Node(4)
print(Node3)

