# Chapter : 7 - item : 2 - หาค่า Min และ Max
#  ส่งมาแล้ว 0 ครั้ง
# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยและมากที่สุดของ Binary Search Tree

# ***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()

# No file chosen
# Submit
# Testcase : #1 1
# Enter Input : 10 4 20 1 5
#       20
#  10
#            5
#       4
#            1
# --------------------------------------------------
# Min : 1
# Max : 20

# Testcase : #2 2
# Enter Input : 4 10 3 6 13 9
#            13
#       10
#                 9
#            6
#  4
#       3
# --------------------------------------------------
# Min : 3
# Max : 13

# Testcase : #3 3
# Enter Input : 1 2 3 4 5 6 7 9 8 0 -1 -2
#                                     9
#                                          8
#                                7
#                           6
#                      5
#                 4
#            3
#       2
#  1
#       0
#            -1
#                 -2
# --------------------------------------------------
# Min : -2
# Max : 9

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
    
    def min(self):
        return self.findMin(self.root)
    
    def findMin(self, node):
        if node.left == None:
            return node
        else:
            return self.findMin(node.left)
    
    def max(self):
        return self.findMax(self.root)
    
    def findMax(self, node):
        if node.right == None:
            return node
        else:
            return self.findMax(node.right)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def printMin(self):
        print('--------------------------------------------------')
        print('Min :', self.min())

    def printMax(self):
        print('Max :', self.max())
        
    def printMinAndMax(self):
        self.printMin()
        self.printMax()

inp = [int(i) for i in input('Enter Input : ').split()]
print(inp)
T = BST()
for i in inp:
    root = T.insert(i)
T.printTree(root)
T.printMinAndMax()