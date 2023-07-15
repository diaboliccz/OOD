class Stack:
  def __init__(self, ls = None):
    self.items = [] if ls == None else ls
  
  def push(self, i):
    self.items.append(i)
  
  def pop(self):
    return self.items.pop()

  def top(self):
    return self.items[-1]
  
  def isEmpty(self):
    return self.size() == 0
  
  def size(self):
    return len(self.items)
  
st = Stack()

class Wood:
  def __init__(self):
    self.stack = Stack()
  
  def stateA(self, height_val):
    temp_stack = Stack()
    for i in self.stack.items:
      if i > height_val:
        temp_stack.push(i)
    self.stack = temp_stack
    self.stack.push(height_val)
  
  def stateB(self):
    return self.stack.size()
  
  def stateS(self):
    for i in range(self.stack.size()):
      if self.stack.items[i]%2 == 0 and self.stack.items[i] > 1:
        self.stack.items[i] -= 1
      else:
        self.stack.items[i] += 2
    self.stateA(self.stack.items[i])
  
  def run(self, input_sent):
    for i in input_sent:
      val = i.split(' ')
      state = val[0]
      if state == 'A':
        self.stateA(int(val[1]))
      elif state == 'B':
        print(self.stateB())
      elif state == 'S':
        self.stateS()

val = input('Enter Input : ').split(',')
wood = Wood()
wood.run(val)
# if not s == ['']:
#   for i in s:
#       if i[0] == 'A' and len(i)>=3:
#           if int(i[2:]) > 0:
#               st.push(int(i[2:]))
#       elif i == 'B' and not st.isEmpty():
#           temp = Stack()
#           if not st.isEmpty():
#               mx = st.pop()
#               temp.push(mx)
#               count = 1
#           else:
#               count = 0
#           while(not st.isEmpty()):
#               value = st.pop()
          
#           temp.push(value)
#           if mx < value:
#               mx = value
#               count += 1
#           print(count)
#           while(not temp.isEmpty()):
#               st.push(temp.pop())
#       elif i == 'S':
#         for j in range(st.size()):
#           if st.items[j]%2 == 0 and st.items[j] > 1:
#             st.items[j] -= 1
#           else:
#             st.items[j] += 2
