class Queue:
    current_time = 0
    highest_wait = {"id": 0, "time": 0}

    def __init__(self, ls=None):
        self.items = ls if ls != None else []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def run(self, log):
        people_list = [[int(i[0]), int(i[1])]
                       for i in [i.split(",") for i in log]]
        people_copy = people_list.copy()
        for i in range(len(people_list)):
            people_list[i].append(i+1)
            people_list[i].append(0)
            people_list[i].append(0)

        main_queue = Queue()
        barista1 = Queue()
        barista2 = Queue()
        while len(people_copy) > 0 or not main_queue.isEmpty() or not barista1.isEmpty() or not barista2.isEmpty():
            done_dict = {}
            for i in people_list:
                if i[0] == self.current_time:
                    main_queue.enqueue(i)
                    people_copy.remove(i)
            if barista1.size() > 0:
                barista1.items[0][3] += 1
                if barista1.items[0][3] == barista1.items[0][1]:
                    done_dict[barista1.items[0][2]] = [self.current_time]
                    done_dict[barista1.items[0][2]].append(1)
                    barista1.dequeue()
            if barista2.size() > 0:
                barista2.items[0][3] += 1
                if barista2.items[0][3] == barista2.items[0][1]:
                    done_dict[barista2.items[0][2]] = [self.current_time]
                    done_dict[barista2.items[0][2]].append(2)
                    barista2.dequeue()
            done_dict = dict(sorted(done_dict.items()))

            for i in main_queue.items:
                i[4] += 1
                if i[4] > self.highest_wait["time"]:
                    self.highest_wait["id"] = i[2]
                    self.highest_wait["time"] = i[4]-1

            if main_queue.size() > 0:
                if barista1.isEmpty():
                    barista1.enqueue(main_queue.dequeue())
                if barista1.size() > 0 and barista2.isEmpty() and not main_queue.isEmpty():
                    barista2.enqueue(main_queue.dequeue())
            for i in done_dict:
                print(f'Time {self.current_time} customer {i} get coffee')
            self.current_time += 1
        if self.highest_wait["time"] == 0:
            print("No waiting")
        else:
            print(
                f"The customer who waited the longest is : {self.highest_wait['id']}\nThe customer waited for {self.highest_wait['time']} minutes")


print(" ***Cafe***")
log_input = input("Log : ").split("/")
q = Queue()
q.run(log_input)
