
def bubbleSort_recur(arr):
    if len(arr) == 1:
        return arr
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    return bubbleSort_recur(arr[:-1]) + [arr[-1]]

inp = input('Enter Input : ').split(' ')
inp = [int(i) for i in inp]
print(bubbleSort_recur(inp))