# class Queue:
#     err_input = 0
#     start_pos = []
#     end_pos = []
#     current_pos = []
#     found = 0

#     def __init__(self, ls=None):
#         self.items = ls if ls != None else []

#     def size(self):
#         return len(self.items)

#     def isEmpty(self):
#         return self.size() == 0

#     def enqueue(self, item):
#         return self.items.append(item)

#     def dequeue(self):
#         return self.items.pop(0) if not self.isEmpty() else None

#     def path_check(self, room, path_prev):
#         current_x = self.current_pos[0][0]
#         current_y = self.current_pos[0][1]
        
#         x = current_x
#         y = current_y
#         if y > 0:
#             y-=1
#             if (x, y) not in self.items and (x, y) not in path_prev.items:
#                 if room[y][x] == '_':
#                     self.enqueue((x, y))
#                 elif room[y][x] == 'O':
#                     self.enqueue((x, y))
#                     self.found = 1
        
#         x = current_x
#         y = current_y
#         if x < len(room[0])-1:
#             x+=1
#             if (x, y) not in self.items and (x, y) not in path_prev.items:
#                 if room[y][x] == '_':
#                     self.enqueue((x, y))
#                 elif room[y][x] == 'O':
#                     self.enqueue((x, y))
#                     self.found = 1
        
#         x = current_x
#         y = current_y
#         if y < len(room)-1:
#             y+=1
#             if (x, y) not in self.items and (x, y) not in path_prev.items:
#                 if room[y][x] == '_':
#                     self.enqueue((x, y))
#                 elif room[y][x] == 'O':
#                     self.enqueue((x, y))
#                     self.found = 1
                
#         x = current_x
#         y = current_y
#         if x > 0:
#             x-=1
#             if (x, y) not in self.items and (x, y) not in path_prev.items:
#                 if room[y][x] == '_':
#                     self.enqueue((x, y))
#                 elif room[y][x] == 'O':
#                     self.enqueue((x, y))
#                     self.found = 1

#     def change_current_pos(self, previous_path):
#         if not self.isEmpty():
#             self.current_pos = [self.dequeue()]
#             previous_path.enqueue(self.current_pos[0])

#     def run(self, val):
#         room_width = int(val[0])
#         room_height = int(val[1])
#         room = [i for i in val[2].split(',')]

#         path_preivios = Queue()

#         if 'F' in val[2]:
#             for i in room:
#                 if len(i) != room_width:
#                     self.err_input = 1
#         else:
#             self.err_input = 1
#         if not self.err_input:
#             for j in range(room_height):
#                 for i in range(room_width):
#                     if room[j][i] == 'F':
#                         self.start_pos.append((i, j))
#                         self.current_pos.append((i, j))
#                         self.enqueue((i, j))
#                     if room[j][i] == 'O':
#                         self.end_pos.append((i, j))
#         else:
#             print("Invalid map input.")
#             return 0
#         print(f'Queue: {self.items}')
#         self.change_current_pos(path_preivios)

#         while self.found == 0:
#             self.path_check(room, path_preivios)
#             if self.end_pos[0] in self.items:
#                 break
#             print(f'Queue: {self.items}')
#             self.change_current_pos(path_preivios)
        
#         # print(f'\nCurrent: {self.current_pos}')
#         # print(f'Exit: {self.end_pos}')
#         # print(f'Previous Queue: {path_preivios.items}')
#         if self.found == 1:
#             print("Found the exit portal.")
#         else:
#             print("Can't reach the exit portal.")

# log = input("Enter width, height, and room: ").split(" ")
# q = Queue()
# q.run(log)

class Queue:
    def __init__(self) -> None:
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0) if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    @property
    def queue(self):
        return self.__items


class SearchPortal:
    def __init__(self) -> None:
        self.queue = Queue()
        self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # Find Position F
    def find_start(self, room):
        for row in room:
            if 'F' in row:
                position = (row.index('F'), room.index(row))
                return position

    def find_the_next_way(self, room):
        x, y = self.queue.dequeue()
        for dx, dy in self.directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_y < len(room) and 0 <= new_x < len(room[0]) and room[new_y][new_x] == 'O':
                return True
            elif 0 <= new_y < len(room) and 0 <= new_x < len(room[0]) and room[new_y][new_x] == '_':
                self.queue.enqueue((new_x, new_y))
                room[new_y][new_x] = 'X'

    def search(self, room):
        self.queue.enqueue(self.find_start(room))
        if None in self.queue.queue:
            return 'Invalid map input.'
        # Main Loop
        while not self.queue.isEmpty():
            print(f'Queue: {self.queue.queue}')
            if self.find_the_next_way(room):
                return 'Found the exit portal.'
        return 'Cannot reach the exit portal.'


def check_valid_room(width, height, room):
    for row in room:
        if len(row) != width:
            return False
    return len(room) == height


width, height, room = input('Enter width, height, and room: ').split()
search_portal = SearchPortal()
room = [list(string) for string in room.split(',')]
if check_valid_room(int(width), int(height), room):
    print(search_portal.search(room))
else:
    print('Invalid map input.')
