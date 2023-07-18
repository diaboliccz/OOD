# class Stack:
#   def __init__(self, ls = None):
#     self.items = [] if ls == None else ls
  
#   def push(self, i):
#     self.items.append(i)
  
#   def pop(self):
#     return self.items.pop()

#   def top(self):
#     return self.items[-1]
  
#   def isEmpty(self):
#     return self.size() == 0
  
#   def size(self):
#     return len(self.items)
  
# st = Stack()

# class Wood:
#   def __init__(self):
#     self.stack = Stack()
  
#   def stateA(self, height_val):
#     temp_stack = Stack()
#     for i in self.stack.items:
#       if i > height_val:
#         temp_stack.push(i)
#     self.stack = temp_stack
#     self.stack.push(height_val)
  
#   def stateB(self):
#     return self.stack.size()
  
#   def stateS(self):
#     for i in range(self.stack.size()):
#       if self.stack.items[i]%2 == 0 and self.stack.items[i] > 1:
#         self.stack.items[i] -= 1
#       else:
#         self.stack.items[i] += 2
#     self.stateA(self.stack.items[i])
  
#   def run(self, input_sent):
#     for i in input_sent:
#       val = i.split(' ')
#       state = val[0]
#       if state == 'A' and int(val[1]) > 0:
#         self.stateA(int(val[1]))
#       elif state == 'B':
#         print(self.stateB())
#       elif state == 'S':
#         self.stateS()

# val = input('Enter Input : ').split(',')
# wood = Wood()
# wood.run(val)
class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        temp = [str(e) for e in self.stack[::]]
        return '[' + ','.join(temp) + ']'

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        val = self.stack[-1]
        del self.stack[-1]
        return val

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

def count_trees(trees):
    stack = Stack()
    for tree in trees:
        try:
            action, h = tree.split()
        except ValueError:
            h = None
            action = tree

        if action == 'A':
            h = int(h)
            stack.push(h)

        elif action == 'B':
            temp = Stack()
            tree_found = 0
            most_height = 0

            while not stack.isEmpty():
                curr_h = stack.pop()
                temp.push(curr_h)
                if curr_h > most_height:
                    tree_found += 1
                    most_height = curr_h

            while not temp.isEmpty():
                stack.push(temp.pop())

            print(tree_found)

        elif action == 'S':
            for i in range(stack.size()):
                if stack.stack[i] % 2 == 0:
                    stack.stack[i] -= 1
                    if stack.stack[i] < 1:
                        stack.stack[i] = 1
                else:
                    stack.stack[i] += 2


command = input('Enter Input : ').split(',')
count_trees(command)