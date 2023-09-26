class Stack:
    def __init__(self, ls = None):
        self.items = ls if ls != None else []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.size() == 0
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop() if not self.isEmpty() else None
    def isMatch(self, log):
        open_bracket = '({['
        close_bracket = ')}]'
        for i in log:
            if i in open_bracket:
                self.push(i)
            elif i in close_bracket:
                if self.isEmpty():
                    return False
                if open_bracket.index(self.pop()) != close_bracket.index(i):
                    return False
        return self.isEmpty()
log = input('Enter Input: ')
st = Stack()
if st.isMatch(log):
    print('Parentheses : Matched ! ! !')
else:
    print("Parentheses : Unmatched ! ! !")
