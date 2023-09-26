inp = input("Enter Input a b : ").split()
a = int(inp[0])
b = int(inp[1])
def pow(a, b):
    if b == 0 and a == 0:
        return None
    if b == 0 and a != 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        return pow(a, b//2) * pow(a, b//2)
    else:
        return pow(a, b//2) * pow(a, b//2) * a
print(pow(a, b))