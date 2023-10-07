def findCloset(arr, target):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr)//2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            return findCloset(arr[:mid], target)
        else:
            return findCloset(arr[mid:], target)


def insertion_sort_recursive(arr_inp, index = 0, arr_out = []):
    if index == len(arr_inp):
        print("sorted")
        return arr_out
    else:
        if len(arr_out) == 0:
            arr_out.append(arr_inp[index])
            # print("insert", arr_inp[index], "at index", index, ":", arr_out, arr_inp[index+1:])
        else:
            if arr_inp[index] < arr_out[0]:
                arr_out.insert(0, arr_inp[index])
                if arr_inp[index+1:] == []:
                    print("insert", arr_inp[index], "at index", 0, ":", arr_out)
                else:
                    print("insert", arr_inp[index], "at index", 0, ":", arr_out, arr_inp[index+1:])
            elif arr_inp[index] > arr_out[-1]:
                arr_out.append(arr_inp[index])
                if arr_inp[index+1:] == []:
                    print("insert", arr_inp[index], "at index", len(arr_out)-1, ":", arr_out)
                else:
                    print("insert", arr_inp[index], "at index", len(arr_out)-1, ":", arr_out, arr_inp[index+1:])
            elif arr_inp[index] > arr_out[0] and arr_inp[index] < arr_out[-1]:
                closet = findCloset(arr_out, arr_inp[index])
                arr_out.insert(arr_out.index(closet)+1, arr_inp[index])
                if arr_inp[index+1:] == []:
                    print("insert", arr_inp[index], "at index", arr_out.index(closet)+1, ":", arr_out)
                else:
                    print("insert", arr_inp[index], "at index", arr_out.index(closet)+1, ":", arr_out, arr_inp[index+1:])
                
        return insertion_sort_recursive(arr_inp, index+1, arr_out)

inp = input("Enter Input : ").split(" ")
inp = [int(i) for i in inp]
inp_sort = insertion_sort_recursive(inp)
print(inp_sort)