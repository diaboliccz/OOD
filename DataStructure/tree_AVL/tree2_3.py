
# # จงเขียนฟังก์ชั่นในการหา Rank ของ input ที่รับเข้ามา โดย Rank คือการแบ่งเป็นชั้นๆตามข้อมูลของ BST โดยจะเริ่มจากค่าที่น้อยกว่าค่าใน BST ที่น้อยที่สุดจะมีค่า Rank = 0 และค่าที่อยู่ตั้งแต่ค่าที่น้อยที่สุดจนถึงตัวถัดไปจะมีค่า Rank +=1 ไปเรื่อยๆจนถึงชั้นของตัวสุดท้ายหรือตัวมากสุด เช่น



# # จากรูป ค่าที่น้อยที่สุดคือ -2 ดังนั้น rank(-2) จะได้ 1 แต่ rank ของค่าที่น้อยกว่า -2 จะเท่ากับ 0

# # และ rank(0) จะเท่ากับ 1 ส่วน rank(1) จะเท่ากับ 2 เป็นต้น

# Enter Input : 1 2 5 4 3 -2/4
#            5
#                 4
#                      3
#       2
#  1
#       -2
# --------------------------------------------------
# Rank of 4 : 5

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        # Code Here
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
        return self.root

    def _insert(self, node, data):
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right == None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
    
    def search(self, data):
        # Code Here
        return self._search(self.root, data)

    def _search(self, node, data):
        if node == None:
            return False
        elif node.data == data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)
    
    def closestValue(self, data):
        # Code Here
        return self._closestValue(self.root, data)
    
    def _closestValue(self, node, data):
        if node == None:
            return None
        elif node.data == data:
            return node.data
        elif data < node.data:
            if node.left == None:
                return node.data
            else:
                return self._closestValue(node.left, data)
        else:
            if node.right == None:
                return node.data
            else:
                return self._closestValue(node.right, data)
    
    def findMin(self):
        # Code Here
        return self._findMin(self.root)
    
    def _findMin(self, node):
        if node.left == None:
            return node.data
        else:
            return self._findMin(node.left)
    
    def rank(self, data):
        # Code Here
        if data == self.findMin():
            return 1
        elif data < self.findMin():
            return 0
        else:
            return self._rank(self.root, data)
        
    def _rank(self, node, data):
        if node == None:
            return 0
        elif node.data == data:
            return self._count(node.left) + 1
        elif data < node.data:
            return self._rank(node.left, data)
        else:
            return self._count(node.left) + 1 + self._rank(node.right, data)
    def _count(self, node):
        if node == None:
            return 0
        else:
            return 1 + self._count(node.left) + self._count(node.right)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)
    
inp = input('Enter Input : ').split('/')
inp1 = [int(i) for i in inp[0].split()]
inp2 = [int(i) for i in inp[1].split()]
tree = BST()
for i in inp1:
    tree.insert(i)
tree.printTree(tree.root)
print('--------------------------------------------------')
print(f'Rank of {inp2[0]} : {tree.rank(inp2[0])}')

