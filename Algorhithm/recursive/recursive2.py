def sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        return arr if arr[0] > arr[1] else [arr[1], arr[0]]
    arr[1:] = sort(arr[1:])
    if arr[0] < arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
        sort(arr)
    return arr

def str_to_int(arr_inp, arr_out=[]):
    if len(arr_inp) == 0:
        return arr_out
    arr_out.append(int(arr_inp[0]))
    return str_to_int(arr_inp[1:], arr_out)

inp = input("Enter your List : ").split(",")
inp_int = str_to_int(inp)
print(f'List after Sorted : {sort(inp_int)}')
