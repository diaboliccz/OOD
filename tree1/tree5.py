# Chapter : 7 - item : 5 - Pretty Tree
#  ส่งมาแล้ว 0 ครั้ง
# ปริ้นต้นไม้ BST เป็นแนวนอน          ที่ครูสอนพี่ฟงนั้นขัดใจ
# อยากให้น้องทำใหม่ช่วยแก้ไข        ให้ต้นไม้ตั้งตรงแตกกิ่งได้
# เลขวรรคขั้นสำหรับข้อมูลรับ            แนะว่านับจำนวนให้ดีไว้
# ทำออกมาให้สวยงามประทับใจ       กฤษฎาอยู่ในป่ายังเชยชม

# *วนลูป insert เลขทีละตัวเข้า tree ตามปกติ < อยู่ซ้าย, >= อยู่ขวา
# No file chosen
# Submit
# Testcase : #1
# Enter input: -1
# -1

# Testcase : #2
# Enter input: -1 -2
#    -1
#   /  
# -2   

# Testcase : #3
# Enter input: -2 -2
# -2   
#   \  
#    -2

# Testcase : #4
# Enter input: 1 2 3 4 5
# 1        
#  \       
#   2      
#    \     
#     3    
#      \   
#       4  
#        \ 
#         5

# Testcase : #5
# Enter input: 5 4 3 2 1
#         5
#        / 
#       4  
#      /   
#     3    
#    /     
#   2      
#  /       
# 1        

# Testcase : #6
# Enter input: 3 2 1 4 5
#     3    
#    / \   
#   2   4  
#  /     \ 
# 1       5

# Testcase : #7
# Enter input: 4 5 3 1 2
#       4  
#      / \ 
#     3   5
#  __/     
# 1        
#  \       
#   2      

# Testcase : #8
# Enter input: 100 120 110 110 130 90 60 70 75 74 76
#                   100                
#                  /   \________       
#                90             120    
#   ____________/          ____/   \   
# 60                    110         130
#   \                      \           
#    70                     110        
#      \___                            
#          75                          
#         /  \                         
#       74    76                       

# Testcase : #9
# Enter input: -100 -120 -110 -110 -130 -90 -60 -70 -75 -74 -76
#                     -100                        
#          __________/    \                       
#      -120                -90                    
#     /    \                  \________________   
# -130      -110                               -60
#               \                             /   
#                -110                      -70    
#                                     ____/       
#                                  -75            
#                                 /   \           
#                              -76     -74        

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
# 1        
#  \       
#   2      
#    \     
#     3    
#      \   
#       4  
#        \ 
#         5
    def printTree(self, node, level=0):
        if node != None:
            print(' ' * level, node.data, end = '\n')
            self.printTree(node.left, level + 1)
            self.printTree(node.right, level + 1)

inp = [int(i) for i in input("Enter Input : ").split()]
T = BST()
for i in inp:
    T.insert(i)
T.printTree(T.root)