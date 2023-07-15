class Stack():
    operator = ['+','-','*','/']
    
    def __init__(self, ls = None):
        self.ls = ls if ls != None else []

    def push(self,i):
        self.ls.append(i)

    def pop(self):
        value = self.ls[-1]
        self.ls.pop()
        return value
        
    def isEmpty(self):
        return len(self.ls) == 0

    def size(self):
        return len(self.ls)
    
def postFixeval(st):

    s = Stack()

    for char in st:
        if char in Stack.operator:
            second_value = s.pop()
            first_value = s.pop()
            if char == '+':
                s.push(first_value + second_value)
            elif char == '-':
                s.push(first_value - second_value)
            elif char == '*':
                s.push(first_value * second_value)
            elif char == '/':
                s.push(first_value / second_value)
        else:
            s.push(float(char))

    return s.pop()


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())


print("Answer : ",'{:.2f}'.format(postFixeval(token)))
