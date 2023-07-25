class Queue:
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

    def run(self, val):
        val_list = [i for i in val.split(" ")]
        people_list = [i for i in val_list[0]]
        main_q = Queue(people_list)
        cashier1_q = Queue()
        cashier2_q = Queue()

        q1_head_checked = {}
        q1_head_count = 0

        q2_head_checked = {}
        q2_head_count = 0
        time_total = int(val_list[1])

        time_current = 1
        for i in range(time_total):
            if not main_q.empty():
                if cashier1_q.qsize() < 5:
                    cashier1_q.enqueue(main_q.dequeue())
                    q1_head_checked[cashier1_q.items[0]] = q1_head_count
                elif cashier1_q.qsize() == 5 and cashier2_q.qsize() < 5:
                    cashier2_q.enqueue(main_q.dequeue())
                    q2_head_checked[cashier2_q.items[0]] = q2_head_count

            print(f'{time_current} {main_q.items} {cashier1_q.items} {cashier2_q.items}')
            if cashier1_q.qsize() > 0:
                q1_head_count += 1
                if q1_head_count == 3:
                    cashier1_q.dequeue()
                    q1_head_count = 0
            if cashier2_q.qsize() > 0:
                q2_head_count += 1
                if q2_head_count == 2:
                    cashier2_q.dequeue()
                    q2_head_count = 0

            time_current += 1


val = input("Enter people and time : ")
q = Queue()
q.run(val)
