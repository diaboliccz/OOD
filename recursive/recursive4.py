
def perket_solver(arr, s=1, b=0, arr_alter=[]):
    if not arr:
        p = None
        if not any(arr_alter):
            p = len(arr_alter)
        else:
            p = 0
        return abs(s - b) * 10 ** p
    print(arr, s, b, arr_alter)
    s_val = arr[0][0]
    b_val = arr[0][1]
    return min(perket_solver(arr[1:], s*s_val, b+b_val, arr_alter+[1]),
               perket_solver(arr[1:], s, b, arr_alter+[0]))

def arr_str_to_int(arr):
    if not arr:
        return []
    a, b = arr[0].split()
    return [[int(a), int(b)]] + arr_str_to_int(arr[1:])


inp = input("Enter Input : ").split(",")
inp = arr_str_to_int(inp)
print(perket_solver(inp))
