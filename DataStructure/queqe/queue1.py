class Queqe:
    def __init__(self, ls = None):
        self.ls = [] if ls is None else ls
    
    def qsize(self):
        return len(self.ls)
    
    def empty(self):
        return self.qsize() == 0
    
    def full(self):
        return self.qsize() == self.maxsize
    
    def enqueue(self, item):
        return self.ls.append(item)
        
    def dequeue(self):
        return self.ls.pop(0)
        
    def run(self, val):
        val_list = [i for i in val.split(",")]
        for i in val_list:
            if i[0] == 'E':
                self.enqueue(i[2:])
                print(f'Add {i[2:]} index is {self.ls.index(i[2:])}')
            elif i[0] == 'D' and not self.empty():
                print(f'Pop {self.dequeue()} size in queue is {self.qsize()}')
            else:
                print(-1)
        
        if self.empty():
            print("Empty")
        else:
            print(f'Number in Queue is :  {self.ls}')
            
input_val = input("Enter Input : ")
q = Queqe()
q.run(input_val)
