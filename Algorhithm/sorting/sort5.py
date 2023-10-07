# Enter Input : 2/-2 3 1 -1 0 -3 2
# [2]
# [-1, 3]
# [0, 2]
# [-3, 2, 3]
# [-2, 1, 3]
# [-1, 0, 3]
# [-1, 1, 2]
# [-3, 0, 2, 3]
# [-2, -1, 2, 3]
# [-2, 0, 1, 3]
# [-1, 0, 1, 2]
# [-3, -1, 1, 2, 3]
# [-2, -1, 0, 2, 3]
# [-3, -1, 0, 1, 2, 3]

def sort_list(inp):
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            if inp[i] > inp[j]:
                inp[i], inp[j] = inp[j], inp[i]
    return inp

def sort_list_from_len(inp):
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            if len(inp[i]) > len(inp[j]):
                inp[i], inp[j] = inp[j], inp[i]
    return inp

def sort_order_and_swap(inp):
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            if len(inp[i]) == len(inp[j]):
                for k in range(len(inp[i])):
                    if inp[i][k] > inp[j][k]:
                        inp[i], inp[j] = inp[j], inp[i]
                        break
    return inp

sum_list = []

dict_list = {}

def generate_sublist_sum(target, inp, index, result, sum):
    # print(f'index: {index}, result: {result}, sum: {sum}')
    if sum == target:
        if sort_list(result) not in sum_list:
            sum_list.append(sort_list(result))
    if index >= len(inp):
        return
    generate_sublist_sum(target, inp, index + 1, result, sum)
    generate_sublist_sum(target, inp, index + 1, result + [inp[index]], sum + inp[index])

inp = input("Enter Input : ").split('/')
inp1 = list(map(int, inp[0].split()))
inp2 = list(map(int, inp[1].split()))

generate_sublist_sum(inp1[0], inp2, 0, [], 0)
sort_list_from_len(sum_list)
sort_order_and_swap(sum_list)

if len(sum_list) == 0:
    print("No Subset")
for i in sum_list:
    # print(i)
    if len(i) not in dict_list:
        dict_list[len(i)] = [i]
    else:
        dict_list[len(i)].append(i)

def sort_dict_in_order(dict_inp):
    for i in dict_inp:
        for j in range(len(dict_inp[i])):
            for k in range(j + 1, len(dict_inp[i])):
                if dict_inp[i][j] > dict_inp[i][k]:
                    dict_inp[i][j], dict_inp[i][k] = dict_inp[i][k], dict_inp[i][j]
    return dict_inp

sort_dict_in_order(dict_list)
        
for i in dict_list:
    for j in dict_list[i]:
        print(j)

# print(dict_list)