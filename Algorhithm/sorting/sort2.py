def findMaxIndex_recursive(arr, start, end):
    if start == end:
        return start
    else:
        minIndex = findMaxIndex_recursive(arr, start+1, end)
        return start if arr[start] > arr[minIndex] else minIndex

def selectionSort_recursive(arr, start, end):
    if start == end:
        return
    else:
        maxIndex = findMaxIndex_recursive(arr, start, end)
        if maxIndex != end:
            arr[maxIndex], arr[end] = arr[end], arr[maxIndex]
            print(f'swap {arr[maxIndex]} <-> {arr[end]} : {arr}')
        selectionSort_recursive(arr, start, end-1)

inp = input('Enter Input : ').split(' ')
inp = [int(i) for i in inp]
selectionSort_recursive(inp, 0, len(inp)-1)
print(inp)
