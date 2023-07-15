print("*** Mod Position ***")
val = input("Enter Input : ").split(",")
sent = val[0]
num = int(val[1])
char_list = []

for i in range(len(sent)):
    if (i+1) % num == 0:
        char_list.append(sent[i])
print(char_list)