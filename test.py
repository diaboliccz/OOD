a = ["1", "2", "3", "5"]
a = list(map(int, a))

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        return arr if arr[0] < arr[1] else [arr[1], arr[0]]
    arr[1:] = merge_sort(arr[1:])
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
        merge_sort(arr)
    return arr
print(merge_sort(a))