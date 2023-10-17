
def bubble_sort(arr, index=0, swap=False):
    if index == len(arr) - 1:
        if not swap:
            return arr
        else:
            return bubble_sort(arr, 0, False)
    else:
        if arr[index] > arr[index + 1]:
            arr[index], arr[index + 1] = arr[index + 1], arr[index]
            return bubble_sort(arr, index + 1, True)
        else:
            return bubble_sort(arr, index + 1, swap)

def selection_sort(arr, index=0, min_index=0):
    if index == len(arr) - 1:
        if min_index != index:
            arr[index], arr[min_index] = arr[min_index], arr[index]
        return arr
    else:
        if arr[index] < arr[min_index]:
            min_index = index
        return selection_sort(arr, index + 1, min_index)

def insertion_sort(arr, index=1):
    if index == len(arr):
        return arr
    else:
        for i in range(index, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            else:
                break
        return insertion_sort(arr, index + 1)

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    if len(left) != 0:
        result += left
    if len(right) != 0:
        result += right
    return result

def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[end], arr[i + 1] = arr[i + 1], arr[end]
    return i + 1

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr



inp = input("Enter the list of numbers: ").split()
inp = list(map(int, inp))
print(inp)