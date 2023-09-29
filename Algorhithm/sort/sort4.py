# พี่ซันฟงต้องการให้น้องๆเรียงลำดับข้อมูลของวานร เพื่อสร้างโปรแกรมเฟ้นหาซีซาร์รุ่นถัดไปมาฟื้นฟูศิวิไลซ์และคัดสรรลิงที่อ่อนแอออกไป

# ห้ามใช้ built-in sort ของ python ให้เขียน sort เอง จะได้ฝึกเขียน

# ให้ใช้ sorting algorithm ที่ time complexity ดีกว่า O(n^2)

# โดยลิงพวกนี้มีข้อมูล 4 อย่างคือ name str int agi

# โดยมีรูปแบบ input คือ (A or D)/attribute_priority/monkey_list

#  - (A or D) คือ Ascending หรือ Descending เพื่อเรียงข้อมูลจากน้อยไปมากหรือมากไปน้อย

#  - attribute_priority คือลำดับความสำคัญของ attribute จากน้อยไปมากขั้นด้วย comma (,)

#  - monkey_list คือข้อมูลของลิงทุกตัว ขั้นด้วย comma ระหว่างลิงแต่ละตัว และขั้นด้วยเว้นวรรคระหว่าง attribute ของลิงเรียงจาก name str int agi

# ตัวอย่าง Input

# D/str,int,agi/caesar 100 10 100,kla 20 110 20,ton 20 111 10,non 20 110 20

# หมายถึง

# D - ให้เรียงจากมากไปน้อย

# str,int,agi - ให้เรียงจาก str ก่อน ถ้า str เท่ากันให้เรียงด้วย int แต่ถ้า int เท่ากันให้เรียงด้วย agi แต่ถ้า agi เท่ากันให้เรียงด้วยตามลำดับ input

# caesar 100 10 100,kla 20 110 20,ton 20 111 10,non 20 110 20

# - ข้อมูลลิงทุกตัว อย่าง caesar จะมี str=100 int=10 agi=100 ส่วน kla จะมี str=20 int=110 agi=20

 

# Output

# list ของลิงที่ sort แล้ว โดยแสดงลิงในรูปแบบ id-name โดย id คือ index ตาม input

# [0-caesar, 2-ton, 1-kla, 3-non]

 

# ooooh ooooh aaaah aaaah phee tem plet jiak jiak

# class Monkey:
#     def __init__(self, name, strength, intelligence, agility, id):
#         self.name = name
#         self.str = strength
#         self.int = intelligence
#         self.agi = agility
#         self.id = id
        
#     def __repr__(self) -> str:
#         pass
# No file chosen
# Submit
# Testcase : #1 Example
# Enter Input: D/str,int,agi/caesar 100 10 100,kla 20 110 20,ton 20 111 10,non 20 110 20
# [0-caesar, 2-ton, 1-kla, 3-non]

# Testcase : #2
# Enter Input: A/agi,name/future 1 99 120,gon 50 50 50,ruth 60 100 80,net 70 98 80,ruth 70 -1 80
# [1-gon, 3-net, 2-ruth, 4-ruth, 0-future]

# Testcase : #3 ¯\_(ツ)_/¯
# Enter Input: D//gon -1 -1 -1,dragon 1000 1000 1000,ryu 100 100 100
# [0-gon, 1-dragon, 2-ryu]

# Testcase : #4 uga uga
# Enter Input: D/str,agi,name,int/z_ton 150 200 80,pune 100 151 130,oat 150 90 90,nit_a 120 1 90,pune 100 150 130,ploy 120 100 100,ya 100 120 130,ton 150 -100 80,john 150 120 150,ya 100 120 130,ton 150 100 80,plaew 120 100 100,pun 100 100 100
# [8-john, 2-oat, 0-z_ton, 10-ton, 7-ton, 5-ploy, 11-plaew, 3-nit_a, 6-ya, 9-ya, 1-pune, 4-pune, 12-pun]

class Monkey:
    def __init__(self, name, strength, intelligence, agility, id):
        self.name = name
        self.str = strength
        self.int = intelligence
        self.agi = agility
        self.id = id
        
    def __repr__(self) -> str:
        return f'{self.id}-{self.name}'
    
    def __lt__(self, other):
        if self.str == other.str:
            if self.int == other.int:
                if self.agi == other.agi:
                    return self.id < other.id
                return self.agi < other.agi
            return self.int < other.int
        return self.str < other.str
    
    def __gt__(self, other):
        if self.str == other.str:
            if self.int == other.int:
                if self.agi == other.agi:
                    return self.id > other.id
                return self.agi > other.agi
            return self.int > other.int
        return self.str > other.str
    
    def __eq__(self, other):
        return self.str == other.str and self.int == other.int and self.agi == other.agi and self.id == other.id
    
    def __le__(self, other):
        return self < other or self == other
    
    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not self == other

def sort_monkey(monkeys, order, attr, index):
    if len(monkeys) == 1:
        return monkeys
    mid = len(monkeys) // 2
    left = sort_monkey(monkeys[:mid], order, attr, index)
    right = sort_monkey(monkeys[mid:], order, attr, index)
    return merge(left, right, order, attr, index)

def merge(left, right, order, attr, index):
    result = []
    while len(left) > 0 and len(right) > 0:
        if order == 'A':
            if getattr(left[0], attr[index]) <= getattr(right[0], attr[index]):
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        else:
            if getattr(left[0], attr[index]) >= getattr(right[0], attr[index]):
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

inp = input("Enter Input: ").split('/')
order = inp[0]
attribute = inp[1].split(',')
monkeys = inp[2].split(',')
monkeys = [Monkey(monkey.split()[0], int(monkey.split()[1]), int(monkey.split()[2]), int(monkey.split()[3]), i) for i, monkey in enumerate(monkeys)]
if attribute != ['']:
    for i in range(len(attribute)-1, -1, -1):
        monkeys = sort_monkey(monkeys, order, attribute, i)
print(monkeys)