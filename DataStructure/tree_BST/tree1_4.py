# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.hd = 0


# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         # Code Here
#         if self.root == None:
#             self.root = Node(data)
#         else:
#             self._insert(self.root, data)
#         return self.root

#     def _insert(self, node, data):
#         if data < node.data:
#             if node.left == None:
#                 node.left = Node(data)
#             else:
#                 self._insert(node.left, data)
#         else:
#             if node.right == None:
#                 node.right = Node(data)
#             else:
#                 self._insert(node.right, data)

#     def index(self, data):
#         # Code Here
#         return self._index(self.root, data)

#     def _index(self, node, data):
#         if node == None:
#             return 0
#         elif node.data == data:
#             return 1
#         else:
#             return self._index(node.left, data) + self._index(node.right, data)

#     def insertNodeAt(self, node, data, index):
#         if node.left == None:
#             node.left = Node(data)
#         elif node.right == None:
#             node.right = Node(data)
#         else:
#             if index == 0:
#                 self.insertNode(node.left, data)
#             else:
#                 self.insertNode(node.right, data)

#     def insertNode(self, node, data):
#         if node.left == None:
#             node.left = Node(data)
#         elif node.right == None:
#             node.right = Node(data)

#     def search(self, data):
#         # Code Here
#         return self.searchNode(self.root, data)

#     def searchNode(self, node, data):
#         if node == None:
#             return False
#         elif node.data == data:
#             return True
#         else:
#             return self.searchNode(node.left, data) or self.searchNode(node.right, data)

#     def goTo(self, node, data):
#         if node == None:
#             return None
#         elif node.data == data:
#             return node
#         else:
#             return self.goTo(node.left, data) or self.goTo(node.right, data)

#     def childCheck(self, node):
#         if node.left == None and node.right == None:
#             return 0
#         elif node.left == None or node.right == None:
#             return 1
#         else:
#             return 2

#     def topView(self):
#         # Code Here
#         return self._topView(self.root)

#     def _topView(self, node):
#         if node == None:
#             return

#         q = []
#         m = dict()
#         hd = 0
#         node.hd = hd
#         q.append(node)
#         while len(q) != 0:
#             node = q[0]
#             hd = node.hd
#             if hd not in m:
#                 m[hd] = node.data
#             if node.left:
#                 node.left.hd = hd - 1
#                 q.append(node.left)
#             if node.right:
#                 node.right.hd = hd + 1
#                 q.append(node.right)
#             q.pop(0)

#         for i in sorted(m):
#             print(m[i], end=' ')

#     def count(self, data):
#         # Code Here
#         return self._count(self.root, data)

#     def _count(self, node, data):
#         if node == None:
#             return 0
#         elif node.data == data:
#             return 1 + self._count(node.left, data) + self._count(node.right, data)
#         else:
#             return self._count(node.left, data) + self._count(node.right, data)

#     def __str__(self) -> str:
#         lines = BST._build_tree_string(self.root, 0, False, "-")[0]
#         return "\n".join((line.rstrip() for line in lines))

#     def _build_tree_string(
#             root: Node,
#             curr_index: int,
#             include_index: bool = False,
#             delimiter: str = "-"):
#         if root is None:
#             return [], 0, 0, 0
#         line1 = []
#         line2 = []
#         if include_index:
#             node_repr = "{}{}{}".format(curr_index, delimiter, root.data)
#         else:
#             node_repr = str(root.data)
#         new_root_width = gap_size = len(node_repr)
#         l_box, l_box_width, l_root_start, l_root_end = \
#             BST._build_tree_string(
#                 root.left, 2 * curr_index + 1, include_index, delimiter)
#         r_box, r_box_width, r_root_start, r_root_end = \
#             BST._build_tree_string(
#                 root.right, 2 * curr_index + 2, include_index, delimiter)
#         if l_box_width > 0:
#             l_root = l_box_width - l_root_end - 1
#             line1.append(" " * (l_box_width + 1))
#             line2.append(" " * (l_box_width - l_root))
#             line2.append("_" * l_root + "/")
#             new_root_start = l_box_width + 1
#             gap_size += 1
#         else:
#             new_root_start = 0
#         line1.append(node_repr)
#         line2.append(" " * new_root_width)
#         if r_box_width > 0:
#             line1.append(" " * (r_box_width + 1))
#             line2.append("\\" + "_" * (r_root_start))
#             line2.append(" " * r_box_width)
#             gap_size += 1
#         new_root_end = new_root_start + new_root_width - 1
#         gap = " " * gap_size
#         new_box = ["".join(line1), "".join(line2)]
#         for i in range(max(len(l_box), len(r_box))):
#             l_line = l_box[i] if i < len(l_box) else " " * l_box_width
#             r_line = r_box[i] if i < len(r_box) else " " * r_box_width
#             new_box.append(l_line + gap + r_line)
#         return new_box, len(new_box[0]), new_root_start, new_root_end


# inp = input('Enter Input : ').split(',')
# inp_root = [i[0] for i in inp]
# inp_val = [i[2:] for i in inp]
# tree = BST()
# for i in range(len(inp_root)):
#     if tree.search(inp_root[i]) == False:
#         tree.insert(inp_root[i])
#     if tree.childCheck(tree.goTo(tree.root, inp_root[i])) < 2:
#         tree.insertNodeAt(
#             tree.goTo(tree.root, inp_root[i]), inp_val[i], tree.index(inp_root[i]))
#     # print('insert :', inp_root[i] + ' -> ' + inp_val[i])
#     # print(tree)
# print('Top view : ', end='')
# tree.topView()

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.val}"

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def is_full(self):
        return self.left and self.right

    def is_empty(self):
        return not (self.left or self.right)


class BST:
    def __init__(self):
        self.root = None

    def top_tree_traverse(self):
        def print_left(root):
            if root:
                print_left(root.left)
                print(root, end=' ')

        def print_right(root):
            if root:
                print(root, end=' ')
                print_right(root.right)

        print_left(self.root)
        print_right(self.root.right)

    def insert_at(self, target, val):
        if not self.root:
            self.root = Node(val)
            return
        target_node = self.search(target)
        if not target_node.left:
            target_node.left = Node(val)
        else:
            target_node.right = Node(val)

    def search(self, kw):
        def _search(root, kw):
            if root:
                if root.val == kw:
                    return root
                found_node = _search(root.left, kw)
                if found_node:
                    return found_node
                found_node = _search(root.right, kw)
                return found_node
            return None

        return _search(self.root, kw)

tree = BST()
inp = [i for i in input('Enter Input : ').split(',')]
tree.root = Node(inp[0].split()[0])
for pair in inp:
    target_node, next_node = pair.split()
    tree.insert_at(target_node, next_node)
print("Top view : ", end="")
tree.top_tree_traverse()
