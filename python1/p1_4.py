# สร้างฟังก์ชันที่รับ input เป็น list(5x5) ของ # และ - โดยแต่ละแฮช (#) แทนทุ่นระเบิดและแต่ละขีด (-) แทนจุดที่ไม่มีทุ่นระเบิด 
# ให้ return list ที่แต่ละขีดถูกแทนที่ด้วยตัวเลขที่ระบุจำนวนของทุ่นระเบิดที่อยู่ติดกับจุดนั้น (แนวนอนแนวตั้งและแนวทแยงมุม)

def num_grid(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            num = 0
            if lst[i][j] == "-":
                if i-1 >= 0 and lst[i-1][j] == "#":
                    num += 1
                if i+1 < len(lst) and lst[i+1][j] == "#":
                    num += 1
                if j-1 >= 0 and lst[i][j-1] == "#":
                    num += 1
                if j+1 < len(lst[i]) and lst[i][j+1] == "#":
                    num += 1
                if i-1 >= 0 and j-1 >= 0 and lst[i-1][j-1] == "#":
                    num += 1
                if i-1 >= 0 and j+1 < len(lst[i]) and lst[i-1][j+1] == "#":
                    num += 1
                if i+1 < len(lst) and j-1 >= 0 and lst[i+1][j-1] == "#":
                    num += 1
                if i+1 < len(lst) and j+1 < len(lst[i]) and lst[i+1][j+1] == "#":
                    num += 1
                lst[i][j] = str(num)
            else:
                lst[i][j] = "#"
    
    return lst

'''lst_input = [

    ["-","-","-","-","-"],

    ["-","-","-","-","-"],

    ["-","-","#","-","-"],

    ["-","-","-","-","-"],

    ["-","-","-","-","-"]

]'''

lst_input = []
print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")

