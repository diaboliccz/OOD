class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __str__(self):
        if self.isEmpty():
            return
        else:
            cur, s = self.head, ''
            while cur is not None:
                s += str(cur.value) + ' '
                cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        if self.isEmpty():
            return 0
        cur = self.head
        i = 1
        while cur.next is not None:
            cur = cur.next
            i += 1
        return i

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addHead(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self, pos):
        i = 0
        if pos < 0:
            pos = self.size() + pos
        if pos >= self.size() or pos < 0:
            return 
        elif pos == 0:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None and i < pos - 1:
                cur = cur.next
                i += 1
            if pos == self.size() - 1:
                self.tail = cur
                self.tail.next = None
            else:
                cur.next = cur.next.next

    def index(self, pos):
        cur = self.head
        i = 0
        while i < pos:
            cur = cur.next
            i += 1
        return cur.value
    
    def insert(self, data, pos):
        new_node = Node(data)
        i = 1
        if pos < 0:
            pos = self.size() + pos
        if self.isEmpty():
            self.head = self.tail = new_node
        elif pos <= 0:
            self.addHead(new_node)
        elif pos >= self.size():
            self.append(new_node)
        else:
            cur = self.head
            while cur.next is not None and i < pos:
                cur = cur.next
                i += 1
            new_node.next = cur.next
            cur.next = new_node

def createLL(ll):
    link = LinkedList()
    for val in ll:
        link.append(val)
    return link

def printLL(head):
    return str(head)

def SIZE(head):
    return head.size()

def bottomUp(head, b):
    for _ in range(b):
        data = head.head.value
        head.pop(0)
        head.append(data)

def deBottomUp(head, b):
    for _ in range(b):
        data = head.tail.value
        head.pop(-1)
        head.addHead(data)

def riffleShuffle(head, r):
    linkedList = LinkedList()
    for i in range(head.size() - r):
        linkedList.addHead(head.tail.value)
        head.pop(-1)
    for i in range(linkedList.size()):
        head.insert(linkedList.head.value, 2 * i + 1)
        linkedList.pop(0)

def deRiffleShuffle(head, r):
    linkedList = LinkedList()
    if r <= head.size() - r:
        for i in range(r):
            linkedList.append(head.index(i))
            head.pop(i)
        for i in range(linkedList.size()):
            head.addHead(linkedList.tail.value)
            linkedList.pop(-1)
    else:
        for i in range(head.size() - r):
            linkedList.append(head.index(i + 1))
            head.pop(i + 1)
        for i in range(linkedList.size()):
            head.append(linkedList.head.value)
            linkedList.pop(0)

def scramble(head, b, r, size):
    bot = int((b / 100) * size)
    riff = int((r / 100) * size)
    bottomUp(head, bot)
    print(f'BottomUp {b:.3f} % :', head)
    riffleShuffle(head, riff)
    print(f'Riffle {r:.3f} % :', head)
    deRiffleShuffle(head, riff)
    print(f'Deriffle {r:.3f} % :', head)
    deBottomUp(head, bot)
    print(f'Debottomup {b:.3f} % :', head)

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scramble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scramble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)