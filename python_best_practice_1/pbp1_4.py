print("*** String Rotation ***")
a, b = input("Enter 2 strings : ").split()
a1 = a
b1 = b
rnd_count = 1
a = a[-1] + a[:-1]
b = b[1:] + b[0]
print(rnd_count, a, b)
while(a1 != a or b1 != b):
  rnd_count += 1
  a = a[-1] + a[:-1]
  b = b[1:] + b[0]
  if rnd_count <= 5:
    print(rnd_count, a, b)

if rnd_count > 6:
  print(" . . . . . ")

if rnd_count > 5:
  print(rnd_count, a, b)

print(f"Total of  {rnd_count} rounds.")