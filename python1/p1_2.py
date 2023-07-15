
print("*** multiplication or sum ***")
value = input("Enter num1 num2 : ").split()
print("The result is", int(value[0]) * int(value[1]) if int(value[0]) * int(value[1]) <= 1000 else int(value[0]) + int(value[1]))