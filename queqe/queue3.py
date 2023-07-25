class Queue:
    err_dq_count = 0
    err_input_count = 0
    ori_items = []
    def __init__(self, items=None):
        self.items = [] if items is None else items
    def qsize(self):
        return len(self.items)
    def empty(self):
        return self.qsize() == 0
    def enqueue(self, item):
        return self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    
    def state(self, val_input):
        state = val_input[0]
        value = val_input[1:]
        state_text = ""
        
        if state == 'E':
            for i in range(int(value)):
                if len(self.ori_items) == 0:
                    self.ori_items.append(f'*{i}')
                else:
                    self.ori_items.append(f'*{int(self.ori_items[-1][1:]) + 1}')
                if self.empty():
                    self.enqueue(self.ori_items[-1])
                else:
                    self.enqueue(self.ori_items[-1])
            state_text = f'Enqueue : {self.items}'
        elif state == 'D':
            for i in range(int(value)):
                if self.qsize() > 0:
                    self.dequeue()
                else:
                    self.err_dq_count += 1
            state_text = f'Dequeue : {self.items}'
        else:
            state_text = self.items
            self.err_input_count += 1
            
        step_text = f'Step : {val_input}'
        err_dq_text = f'Error Dequeue : {self.err_dq_count}'
        err_input = f'Error input : {self.err_input_count}'
        print(f'{step_text}\n{state_text}\n{err_dq_text}\n{err_input}')
        print('--------------------')

    def run(self, val):
        for i in val:
            self.state(i)
    
val = input("input : ").split(",")
q = Queue()
q.run(val)