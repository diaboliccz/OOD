
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.linkedlistsize = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, ""
        while cur != None:
            s += str(cur.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.isEmpty():
            self.head = Node(item)
            self.tail = self.head
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(item)
            cur.next.previous = cur
            self.tail = cur.next
            self.tail.previous = cur
            self.tail.next = None

    def addHead(self, item):
        if self.isEmpty():
            self.head = Node(item)
            self.tail = self.head
        else:
            self.head.previous = Node(item)
            self.head.previous.next = self.head
            self.head = self.head.previous
            self.head.previous = None

    def insert(self, pos, item):
        if pos > self.size():
            self.append(item)
        elif pos == 0 or self.isEmpty() or abs(pos) >= self.size():
            self.addHead(item)
        else:
            if pos < 0:
                pos = self.size() + pos
            count = 0
            cur = self.head
            while cur:
                if count == pos:
                    node = Node(item)
                    node.next = cur
                    node.previous = cur.previous
                    cur.previous.next = node
                    cur.previous = node
                    break
                cur = cur.next
                count += 1

    def search(self, item):
        if self.isEmpty():
            return "Not Found"
        else:
            cur = self.head
            while cur != None:
                if cur.value == item:
                    return "Found"
                cur = cur.next
            return "Not Found"

    def index(self, item):
        if self.isEmpty():
            return -1
        else:
            cur = self.head
            for i in range(self.size()):
                if cur.value == item:
                    return i
                if cur.next != None:
                    cur = cur.next
            return -1

    def size(self):
        t = self.head
        length = 0
        while t != None:
            t = t.next
            length += 1
        return length

    def pop(self, pos):
        if pos < 0 or pos > self.size()-1 or self.isEmpty():
            return "Out of Range"
        elif pos == 0:
            self.head = self.head.next
            if self.head != None:
                self.head.previous = None
            return "Success"
        elif pos == self.size():
            self.tail = self.tail.previous
            self.tail.next = None
            return "Success"
        else:
            cur = self.head
            for i in range(pos):
                cur = cur.next
                i += 1
            cur.previous.next = cur.next
            cur.next.previous = cur.previous
            return "Success"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print(f"{L.search(i[3:])} {i[3:]} in {L}")
    elif i[:2] == "SI":
        print(f"Linked List size = {L.size()} : {L}")
    elif i[:2] == "ID":
        print(f"Index ({i[3:]}) = {L.index(i[3:])} : {L}")
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print((f"{k} | {before}-> {L}") if k == "Success" else (f"{k} | {L}"))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
