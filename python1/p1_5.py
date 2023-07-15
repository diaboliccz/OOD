
print("*** Fun with countdown ***")
value = input("Enter List : ").split()

value = [int(i) for i in value]


def countdown(lst):
    count = 0
    result = []
    count_round = 0
    
    for i in range(len(lst)):
        if lst[i] == 1:
            count += 1
            result.append([])
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1] + 1:
            result[count_round].append(lst[i])
        elif lst[i] == 1:
            result[count_round].append(lst[i])
            count_round += 1
    if lst[-1] == 1:
        result[count_round].append(lst[-1])

    return [count, result]

print(countdown(value))