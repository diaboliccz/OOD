# Chapter : 7 - item : 3 - สีแดงแรง 3 เท่า
#  ส่งมาแล้ว 0 ครั้ง
# ให้น้องๆรับ input เป็น list และ k โดยให้สร้าง Binary Search Tree จาก list ที่รับมา และหลังจากนั้นให้ทำการดูว่าใน Tree มีค่าไหนที่มากกว่าค่า k หรือไม่ ถ้ามีให้ทำการคูณ 3 เพิ่มเข้าไป

# No file chosen
# Submit
# Testcase : #1 1
# Enter Input : 67 102 81 35 15 7 99 196 202 152/90
#                 202
#            196
#                 152
#       102
#                 99
#            81
#  67
#       35
#            15
#                 7
# --------------------------------------------------
#                 606
#            588
#                 456
#       306
#                 297
#            81
#  67
#       35
#            15
#                 7

# Testcase : #2 2
# Enter Input : 5 3 -1 4 7 6 8/-5
#            8
#       7
#            6
#  5
#            4
#       3
#            -1
# --------------------------------------------------
#            24
#       21
#            18
#  15
#            12
#       9
#            -3

# Testcase : #3 3
# Enter Input : 5 3 1 4 7 6 8/4
#            8
#       7
#            6
#  5
#            4
#       3
#            1
# --------------------------------------------------
#            24
#       21
#            18
#  15
#            4
#       3
#            1

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        # Code Here
        if self.root == None:
            self.root = Node(data)
        else:
            self.insertNode(self.root, data)
        return self.root

    def insertNode(self, node, data):
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                self.insertNode(node.left, data)
        else:
            if node.right == None:
                node.right = Node(data)
            else:
                self.insertNode(node.right, data)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def mul(self, node, k):
        if node != None:
            if int(node.data) > k:
                node.data = (int(node.data) * 3)
            self.mul(node.left, k)
            self.mul(node.right, k)
    
    def printMul(self, node, level = 0):
        if node != None:
            self.printMul(node.right, level + 1)
            print('     ' * level, node)
            self.printMul(node.left, level + 1)
    
inp = input("Enter Input : ").split('/')
inp_val = [int(i) for i in inp[0].split()]
inp_mul = int(inp[1])
T = BST()
for i in inp_val:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
T.mul(root, inp_mul)
T.printMul(root)
