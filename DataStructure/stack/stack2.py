value = input("Enter Input : ").split(",")
value = [i.split() for i in value]
for i in value:
    if i[0] != "P":
        value[value.index(i)] = [i[0],int(i[-1])]
def ManageStack(value):
    stack = []
    for i in value:
        if i[0] == "A":
            stack.append(i[1])
            print("Add =",i[1])
        elif i[0] == "P":
            if len(stack) == 0:
                print("-1")
            else:
                print("Pop =",stack[-1])
                stack.pop()
        elif i[0] == "D":
            if len(stack) == 0:
                print("-1")
            elif i[1] in stack:
                temp = [j for j in stack if j == i[-1]]
                stack = [j for j in stack if j != i[-1]]
                for j in temp:
                    print(f"Delete = {j}")
        elif i[0] == "LD":
            if len(stack) == 0:
                print("-1")
            else:
                temp = [j for j in stack if j < i[-1]]
                temp.reverse()
                stack = [j for j in stack if j >= i[-1]]
                for j in temp:
                    print(f"Delete = {j} Because {j} is less than {i[-1]}")
        elif i[0] == "MD":
            if len(stack) == 0:
                print("-1")
            else:
                temp = [j for j in stack if j > i[-1]]
                temp.reverse()
                temp.reverse()
                stack = [j for j in stack if j <= i[-1]]
                for j in temp:
                    print(f"Delete = {j} Because {j} is more than {i[-1]}")
    print("Value in Stack =",stack)
ManageStack(value)