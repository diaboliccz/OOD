
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.active = True

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s += '->' + str(cur.next.value)
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None
    
    def getHead(self):
        return self.head.value
    
    def getTail(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        return cur.value

    def append(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node

    def appendList(self, list):
        if self.isEmpty():
            self.head = list.head
        else:
            cur = self.head
            while cur.next.value != list.head.value:
                cur = cur.next
            cur.next = list.head

    def addHead(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

n, train_node = input('Enter input: ').split(' ')
n = int(n)
train_node = train_node.split(',')
unused_node = list(range(1,n+1))

train_list = list()
for i in train_node:
    h, t = [int(x) for x in i.split('-')]
    for train in train_list:
        if train.getTail() == h:
            if t in unused_node:
                unused_node.remove(t)
            train.append(t)
            n-=1
            break

        if train.getHead() == t:
            if h in unused_node:
                unused_node.remove(h)
            train.addHead(h)
            n-=1
            break
    else:
        if h in unused_node:
            unused_node.remove(h)
        if t in unused_node:
            unused_node.remove(t)
        new_train = LinkedList()
        new_train.append(h)
        new_train.append(t)
        n -= 2
        train_list.append(new_train)

remove_train = list()
for train_h in train_list:
    for train_t in train_list:
        if train_h.active and train_t.active and train_h.getTail() == train_t.getHead():
            train_h.appendList(train_t)
            train_t.active = False
            n += 1
            remove_train.append(train_t)

for train in remove_train:
    train_list.remove(train)

train_list = sorted(train_list, key=lambda x: x.head.value)
num_train = len(train_list) + n

for i in range(1,num_train+1):
    if unused_node and train_list:
        if unused_node[0] < train_list[0].head.value:
            print(f'{i}: {unused_node.pop(0)}')
        else:
            print(f'{i}: {train_list.pop(0)}')
    elif unused_node:
        print(f'{i}: {unused_node.pop(0)}')
    else:
        print(f'{i}: {train_list.pop(0)}')
        
print(f'Number of train(s): {num_train}')