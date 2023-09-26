class StackCalc():
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
    
    def run(self, arg):
        self.arg = arg
        for char in self.arg:
            if char.isalpha() and char != 'DUP' and char != 'POP':
                print("Invalid instruction: " + char)
            if char in StackCalc.operator:
                second_value = self.pop()
                first_value = self.pop()
                if char == '+':
                    self.push(first_value + second_value)
                elif char == '-':
                    self.push(second_value - first_value)
                elif char == '*':
                    self.push(first_value * second_value)
                elif char == '/':
                    self.push(int(second_value / first_value))
            elif char == 'DUP':
                self.push(self.ls[-1])
            elif char == 'POP':
                self.pop()
            elif char == 'PSH':
                self.push(int(char))
            else:
                self.push(int(char))
    
    def getValue(self):
        value = self.ls[-1] if len(self.ls) != 0 else 0
        return value

print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())