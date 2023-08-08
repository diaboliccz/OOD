# สร้าง method insert ในคลาส LinkedList เพื่อแทรกข้อมูลลงใน index ที่กำหนดของ linked list และ return ผลลัพธ์ตามตัวอย่าง

# โดยคลาส LinkedList จะประกอบไปด้วย

# 1. def __init__(self): สำหรับสร้าง linked list

# 2. def __str__(self): return string แสดง ค่าใน linked list

# 3. def isEmpty(self): return list นั้นว่างหรือไม่

# 4. def append(self, data): เพิ่ม data ต่อท้าย linked list

# 5. def insert(self, index, data): insert data ใน index ที่กำหนด

# โดยการแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่

# คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Header Node ดูนะครับ

# *******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********

# class Node:
#     def __init__(self, data):
#         self.data = data


# ข้อมูลอินพุท จะคั่นด้วยเครื่องหมาย คอมม่า

# ตัวแรก จะเป็น ลิสต์ตั้งต้น คั่นด้วยช่องว่าง (space)

# ตัวต่อไปจะอยู่ในรูปแบบ index:data

# Enter Input : 1 2 3 4, 0:7, 3:9
# ลิสต์ตั้งต้นคือ 1->2->3->4

# ข้อมูล 0:7 คือให้เพิ่ม node ลำดับ 0 โดยมีข้อมูลเป็น 7

# ข้อมูล 3:9 คือให้เพิ่ม node ลำดับ 3 โดยมีข้อมูลเป็น 9

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next if next != None else None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "empty"
        cur, s = self.head, str(self.head.data) + "->"
        while cur.next != None:
            s += str(cur.next.data) + "->"
            cur = cur.next
        return s[:-2]

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        if self.isEmpty():
            self.head = Node(data)
            self.size += 1
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(data)
            self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            print(f"Data cannot be added")
        elif index == 0:
            self.head = Node(data, self.head)
            self.size += 1
            print(f"index = {index} and data = {data}")
        else:
            cur, i = self.head, 0
            while i != index - 1:
                cur = cur.next
                i += 1
            cur.next = Node(data, cur.next)
            self.size += 1
            print(f"index = {index} and data = {data}")
            
        if self.size != 0:
            print(f"link list : {self}")
        else:
            print(f'List is {self}')

linked_list_start = None
log = input("Enter Input : ").split(",")

start_log = [i for i in log[0].split()]
operate_log = [i for i in log[1:]]
linked_list_start = LinkedList()

for i in start_log:
    linked_list_start.append(i)
if linked_list_start.size != 0:
    print(f"link list : {linked_list_start}")
else:
    print(f'List is {linked_list_start}')
    
    
for i in operate_log:
    index, data = i.split(":")
    linked_list_start.insert(int(index), data)
