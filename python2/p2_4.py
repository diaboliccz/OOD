def hbd(age):
    num = age//2
    f = num
    l = age%num
    result = f'saimai is just 2{l}, in base {f}!'
    return result

year = input("Enter year : ")
print(hbd(int(year)))