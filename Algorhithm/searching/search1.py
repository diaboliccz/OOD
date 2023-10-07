
inp = input("input : ").split(",")
width = int(inp[0].split(" ")[0])
height = int(inp[0].split(" ")[1])
table = inp[1].split(" ")
table = [int(i) for i in table]
table = [table[i:i+width] for i in range(0,len(table),width)]

# for i in table:
#     print(i)

def find_min_val_and_row(table):
    
    min_val = table[0][0]
    min_row = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] < min_val:
                min_val = table[i][j]
                min_row = i
    return (min_val,min_row)

def find_max_val_and_col_from_row(table, row):
    max_val = table[row][0]
    max_col = 0
    for i in range(len(table[row])):
        if table[row][i] > max_val:
            max_val = table[row][i]
            max_col = i
    return (max_val,max_col)

min_row = find_min_val_and_row(table)[1]

def find_max_val_from_col(table,col):
    max_val = table[0][col]
    for i in range(len(table)):
        if table[i][col] > max_val:
            max_val = table[i][col]
    return max_val

max_col = find_max_val_and_col_from_row(table,min_row)[1]

print(find_max_val_from_col(table,max_col))