# Jean รักษาการผู้บัญชาการของกองอัศวิน Favonius แห่ง Mondstadt ต้องการทราบถึงขุมพลังของอัศวินในแต่ละกลุ่มภายในเมือง Mondstadt แห่งนี้จึงจะทดสอบความแข็งแกร่งของขุมกำลังที่มี โดยจะทำการจัดวางกำลังอัศวินภายในเมือง Mondstadt ดังตัวอย่างต่อไปนี้
#                 พลัง    :   5  4  4  3  2  2  2
#                 ลำดับ  :   0  1  2  3  4  5  6
# จากข้อมูลข้างต้นประกอบด้วยอัศวินทั้งหมด 7 คน เรียงตามลำดับตั้งแต่ลำดับที่ 0 ถึง 6 และพลังของอัศวินแต่ละคนมีข้อกำหนดดังนี้
#     -  อัศวินลำดับที่ n จะมีลูกน้องในสังกัดอยู่ลำดับที่ 2n+1 และ 2n+2 (ลูกน้องของลูกน้องของอัศวินลำดับที่ n ถือว่าเป็นลูกน้องของอัศวินลำดับที่ n ด้วย)
#     -  ค่าพลังของอัศวินมีค่าตั้งแต่ 0 - 5
#     -  กลุ่มของอัศวินกลุ่มที่ i จะมีสมาชิกคือ อัศวินลำดับที่ i และลูกน้องของอัศวินลำดับที่ i (รวมลูกน้องของลูกน้องของอัศวินด้วย)
#     -  พลังของกลุ่มอัศวินลำดับที่ i เป็นพลังรวมของสมาชิกของอัศวินทั้งหมดในกลุ่ม เช่น
#             -  อัศวินกลุ่มที่ 1 หมายถึง กลุ่มของอัศวินลำดับที่ 1 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 1, 3 และ 4 และค่าพลังรวมของอัศวินกลุ่มที่ 1 เท่ากับ 4 + 3 + 2 = 9
#             -  อัศวินกลุ่มที่ 2 หมายถึง กลุ่มของอัศวินลำดับที่ 2 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 2 , 5 และ 6 และค่าพลังรวมของอัศวินกลุ่มที่ 2 เท่ากับ 4 + 2 + 2 = 8

# ดังนั้นเมื่อนำพลังของอัศวินกลุ่มที่ 1 และ 2 มาเทียบกัน จะได้ว่าพลังรวมของอัศวินกลุ่มที่ 1 นั้นมากกว่าพลังรวมของอัศวินกลุ่มที่ 2
# Jean ต้องการทราบว่าค่าพลังรวมของอัศวินภายในเมือง Mondstadt เป็นเท่าใด และถ้าเปรียบเทียบระหว่างอัศวินแต่ละกลุ่มแล้วค่าของพลังรวมของอัศวินในกลุ่มใดมีค่ามากกว่ากัน

class BST:
    order = 0

    class Node:
        order = 0

        def __init__(self, data):
            self.data = [BST.order, data]
            self.left, self.right = None, None
            self.parent = None
            BST.order += 1

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = self.Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if BST.order == 2*node.data[0] + 1:
            node.left = self.Node(data)
        elif BST.order == 2*node.data[0] + 2:
            node.right = self.Node(data)
        else:
            index = (BST.order-1)//2
            node = self._goTo_index(self.root, index)
            if BST.order == 2*node.data[0] + 1:
                node.left = self.Node(data)
            elif BST.order == 2*node.data[0] + 2:
                node.right = self.Node(data)
        if node.left != None:
            node.left.parent = node
        if node.right != None:
            node.right.parent = node

    def _count(self, node):
        if node == None:
            return 0
        else:
            return 1 + self._count(node.left) + self._count(node.right)

    def goTo_index(self, data):
        return self._goTo_index(self.root, data)

    def _goTo_index(self, node, data):
        if node == None:
            return None
        elif node.data[0] == data:
            return node
        else:
            return self._goTo_index(node.left, data) or self._goTo_index(node.right, data)

    def sum_parent(self, data):
        node = self.goTo_index(data)
        if node == None:
            return 0
        else:
            data_parent = node.parent.data[1] if node.parent != None else 0
            return data_parent + node.data[1]

    def sum_children(self, data):
        node = self.goTo_index(data)
        if node == None:
            return 0
        else:
            data_left = node.left.data[1] if node.left != None else 0
            data_right = node.right.data[1] if node.right != None else 0
            return data_left + data_right

    def sum_group(self, data):
        node = self.goTo_index(data)
        if node == None:
            return 0
        else:
            return node.data[1] + self.sum_children(data)

    def __str__(self) -> str:
        lines = BST._build_tree_string(self.root, 0, False, "-")[0]
        return "\n".join((line.rstrip() for line in lines))

    def _build_tree_string(
            root: Node,
            curr_index: int,
            include_index: bool = False,
            delimiter: str = "-"):
        if root is None:
            return [], 0, 0, 0
        line1 = []
        line2 = []
        if include_index:
            node_repr = "{}{}{}".format(curr_index, delimiter, root.data)
        else:
            node_repr = str(root.data)
        new_root_width = gap_size = len(node_repr)
        l_box, l_box_width, l_root_start, l_root_end = \
            BST._build_tree_string(
                root.left, 2 * curr_index + 1, include_index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            BST._build_tree_string(
                root.right, 2 * curr_index + 2, include_index, delimiter)
        if l_box_width > 0:
            l_root = l_box_width - l_root_end - 1
            line1.append(" " * (l_box_width + 1))
            line2.append(" " * (l_box_width - l_root))
            line2.append("_" * l_root + "/")
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0
        line1.append(node_repr)
        line2.append(" " * new_root_width)
        if r_box_width > 0:
            line1.append(" " * (r_box_width + 1))
            line2.append("\\" + "_" * (r_root_start))
            line2.append(" " * r_box_width)
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1
        gap = " " * gap_size
        new_box = ["".join(line1), "".join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else " " * l_box_width
            r_line = r_box[i] if i < len(r_box) else " " * r_box_width
            new_box.append(l_line + gap + r_line)
        return new_box, len(new_box[0]), new_root_start, new_root_end


inp = input('Enter Input : ').split('/')
inp1 = [int(i) for i in inp[0].split()]
inp2 = [[int(i[0]), int(i[2:])] for i in inp[1].split(',')]
tree = BST()
print(sum(inp1))
for i in range(len(inp1)):
    tree.insert(inp1[i])
# for i in range(len(inp1)):
#     print(f'Sum Group of {i} = {tree.sum_group(i)}')
for i in range(len(inp2)):
    if tree.sum_group(inp2[i][0]) > tree.sum_group(inp2[i][1]):
        print(f'{inp2[i][0]}>{inp2[i][1]}')
    elif tree.sum_group(inp2[i][0]) < tree.sum_group(inp2[i][1]):
        print(f'{inp2[i][0]}<{inp2[i][1]}')
    else:
        print(f'{inp2[i][0]}={inp2[i][1]}')

# print(tree)
