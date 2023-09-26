class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def __str__(self):
		if self.isEmpty():
			return "Empty"
		cur, s = self.head, ""
		while cur != None:
			if cur.next == None:
				s += str(cur.value)
			else:
				s += str(cur.value) + "->"
			cur = cur.next
		return s

	def isEmpty(self):
		return self.head == None

	def append(self, item):
		new_node = Node(item)
		if self.isEmpty():
			self.head = new_node
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = new_node

	def addHead(self, item):
		new_node = Node(item)
		if self.isEmpty():
			self.head = new_node
		else:
			new_node.next,self.head = self.head,new_node

	def search(self, item):
		curr = self.head
		while curr and curr.value != item:
			curr = curr.next
		if not curr:
			return f"Not Found {item}"
		return f"Found {item}"

	def index(self, item):
		curr,cnt = self.head,0
		while curr and curr.value != item:
			curr = curr.next
			cnt += 1
		if not curr:
			return -1
		return cnt

	def size(self):
		if self.isEmpty():
			return 0
		curr,cnt = self.head,0
		while curr:
			curr = curr.next
			cnt += 1
		return cnt

	def pop(self, pos):
		curr, i = self.head, 0
		if self.isEmpty():
			return "Out of Range"
		if pos == 0:
			self.head = curr.next
			return "Success"
		while curr.next:
			if i == pos - 1:
				curr.next = curr.next.next
				return "Success"
			i += 1
			curr = curr.next
		return "Out of Range"

	def	is_loop(self):
		curr = self.head
		history = []
		while curr:
			if curr in history:
				return 1
			history.append(curr)
			curr = curr.next
		return 0
	
	def	set_node(self, src, dst):
		size = self.size()
		i,curr = 0, self.head
		dst_node = None
		src_node = None
		if self.isEmpty():
			print("Error! {list is empty}")
			return 1
		elif src >= size:
			print("Error! {index not in length}: ", end="")
			print(src)
			return 1
		elif dst >= size:
			print(f"index not in length, append : {dst}")
			self.append(dst)
			return 1
		while i < size and curr:
			if i == src:
				src_node = curr
			if i == dst:
				dst_node = curr
			curr = curr.next
			i += 1
		if  src_node and dst_node:
			src_node.next = dst_node
			print(f"Set node.next complete!, index:value = {src}:{src_node.value} -> {dst}:{dst_node.value}")
			return 1


inp = input('Enter input : ')
L = LinkedList()
inp = inp.split(',')
for i in inp:
	mode,param = i.split()
	if mode == "A":
		L.append(param)
		print(L)
	elif mode == "S":
		src,dst = param.split(':')
		L.set_node(int(src), int(dst))
if L.is_loop():
	print("Found Loop")
else:
	print("No Loop")
	print(L)