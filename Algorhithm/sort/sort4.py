
def insertionSort_recursive(arr, n):
    if n <= 1:
        return
    insertionSort_recursive(arr, n-1)
    last = arr[n-1]
    j = n-2
    while (j >= 0 and arr[j] > last):
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = last

inp = input('Enter Input : ').split(' ')
inp = [int(i) for i in inp]
