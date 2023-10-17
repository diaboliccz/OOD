
class Node:
     def __init__(self, data, freq, left = None, right = None) -> None:
          self.data = data
          self.freq = freq
          self.left = left
          self.right = right

     def __str__(self) -> str:
         return str(self.data)

class HuffmanTree:
     def __init__(self) -> None:
          self.root = None

     def insert(self, root: Node, data:str, freq:int) -> Node:
          if not root:
             return Node(data, freq)
          elif freq < root.freq:
              root.left = self.insert(root.left,data,freq)
          elif freq == root.freq:
               if data < root.data:
                    root.left = self.insert(root.left, data, freq)
               else:
                    root.right = self.insert(root.right, data, freq)
          else:
              root.right = self.insert(root.right, data, freq)
          return root

     def inorder(self, root: Node) -> list:
          if not root:
               return []
          return  self.inorder(root.right)+ [Node(root.data, root.freq)]+ self.inorder(root.left)


def print_tree(node: Node, level: int = 0) -> None:
     if node != None:
          print_tree(node.right, level + 1)
          print('     ' * level, node)
          print_tree(node.left, level + 1)

def get_code(root: Node, code: str) -> str:
     s = ''
     if root:
          s = get_code(root.right, code + '1')
          if root.data != '*':
               s += "'" + str(root.data) + "': '" + code + "'"
          a = get_code(root.left, code + '0')
          if a != '':
               s += ', ' + a
     return s

def search(root: Node, data: str, code: str) -> str: 
     if not root:
          return None
     if data == root.data:
          return code
     if root:
          s = search(root.right, data, code + '1')
          if s != None:
               return s
          s = search(root.left, data, code + '0')
          return s               


inp = [x for x in input('Enter Input : ')]
s = set(inp)
huffman = HuffmanTree()
for i in s:
     huffman.root = huffman.insert(huffman.root, i, inp.count(i))
data = huffman.inorder(huffman.root)
temp = [data.pop()]
while len(data) != 0 or len(temp) != 1:
     if len(temp) > 1:
          if data == [] or (data[-1].freq >= temp[0].freq + temp[1].freq):
               a, b = temp.pop(0), temp.pop(0)
               temp.append(Node('*',a.freq + b.freq, a, b))
          else:
               temp.append(data.pop())
     else:
          temp.append(data.pop())

print('{' + f'{get_code(temp[0], "")}' + '}') 
print_tree(temp[0])
print('Encoded! : ', end = '')
for i in inp:
     print(search(temp[0], i, ''), end = '')