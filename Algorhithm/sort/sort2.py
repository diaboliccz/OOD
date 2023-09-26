
def minIndex( a , i , j ):
    if i == j:
        return i
    k = minIndex(a, i + 1, j)
    return (i if a[i] < a[k] else k)

# Recursive selection sort. n is
# size of a[] and index is index of
# starting element.
def recurSelectionSort(a, n, index = 0):

    # Return when starting and
    # size are same
    if index == n:
        return -1

    # calling minimum index function
    # for minimum index
    k = minIndex(a, index, n-1)

    if k != index:
        print(k, index)
        print(f'swap {a[k]} <-> {a[index]} : {a}')
        a[k], a[index] = a[index], a[k]

    recurSelectionSort(a, n, index + 1)


inp = input('Enter Input : ').split(' ')
inp = [int(i) for i in inp]
recurSelectionSort(inp, len(inp))
print(inp)