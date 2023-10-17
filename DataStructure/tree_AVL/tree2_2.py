# จงเขียนฟังก์ชั่นสำหรับการ insert แบบ Binary Search Tree (BST) โดยที่ input ตัวแรกจะเป็น root เสมอและจงเขียนฟังก์ชั่นสำหรับการหาค่าที่ใกล้เคียง input ที่รับเข้ามาที่สุดที่อยู่ใน BST ที่ทำการ insert ครบแล้ว

# รูปแบบการรับ input จะแบ่งโดย '/'

# 1.ชุดของ BST ที่จะทำการ insert โดยตัวแรกจะเป็น root เสมอ

# 2.ค่าที่จะนำมาเปรียบเทียบกับค่าใน BST ที่ทำการ insert แล้ว

# รูปแบบ output

# จะ printTree ทุกครั้งที่มีการ insert ค่าเข้าและเมื่อทำการ insert จบจะเรียกใช้ฟังก์ชั่น closestValue(root,value) และแสดงค่าที่ใกล้เคียงที่สุดจาก BST

# *** ถ้าหากค่าที่รับเข้ามาเทียบมีอยู่ใน BST ให้ return ค่านั้นออกมาได้เลย และหากมีค่าที่อยู่ใกล้มากกว่า 1 จำนวนให้แสดงจำนวนที่มากที่สุดที่อยู่ใกล้ค่านั้น ***

# Testcase : #1 1
# Enter Input : 1 2 5 4 3 -2 -1/0
#  1
# --------------------------------------------------
#       2
#  1
# --------------------------------------------------
#            5
#       2
#  1
# --------------------------------------------------
#            5
#                 4
#       2
#  1
# --------------------------------------------------
#            5
#                 4
#                      3
#       2
#  1
# --------------------------------------------------
#            5
#                 4
#                      3
#       2
#  1
#       -2
# --------------------------------------------------
#            5
#                 4
#                      3
#       2
#  1
#            -1
#       -2
# --------------------------------------------------
# Closest value of 0 : 1

class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        if self.root == None:
            self.root = self.Node(data)
        else:
            self._insert(self.root, data)
        return self.root

    def _insert(self, node, data):
        if data < node.data:
            if node.left == None:
                node.left = self.Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right == None:
                node.right = self.Node(data)
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

    def findMin(self, node):
        if node.left == None:
            return node
        else:
            return self.findMin(node.left)

    def findMax(self, node):
        if node.right == None:
            return node
        else:
            return self.findMax(node.right)

    def closetValue(self, data):
        diff = []
        for i in range(self.findMin(self.root).data, self.findMax(self.root).data+1):
            if self.search(i):
                diff.append([data, i, abs(i-data)])
        min_val = min(diff, key=lambda x: x[2])[2]
        diff = [i[1] for i in diff if i[2] == min_val]
        return max(diff, key=lambda x: x)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level+1)
            print("     "*level, node.data)
            self.printTree(node.left, level+1)


inp = input('Enter Input : ').split('/')
inp1 = [int(i) for i in inp[0].split()]
inp2 = [int(i) for i in inp[1].split()]
tree = BST()
for i in inp1:
    tree.insert(i)
    tree.printTree(tree.root)
    print('--------------------------------------------------')
print('Closest value of {} : {}'.format(inp2[0], tree.closetValue(inp2[0])))
