def bubble_sort_recursive(arr, index=0, swapped=False):
    if index == len(arr) - 1:
        if not swapped:
            return arr
        else:
            return bubble_sort_recursive(arr, 0, False)
    else:
        if arr[index] > arr[index + 1]:
            arr[index], arr[index + 1] = arr[index + 1], arr[index]
            return bubble_sort_recursive(arr, index + 1, True)
        else:
            return bubble_sort_recursive(arr, index + 1, swapped)

# Test the function
inp = input("Enter Input : ").split()
arr = list(map(int, inp))
bubble_sort_recursive(arr)
print(arr)
