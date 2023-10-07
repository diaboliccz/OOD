
inp = input("Data : ").split()
inp = [int(i) for i in inp]
out = []
max_len = []
def LIS(inp):
    global max_len
    for i in range(len(inp)):
        if i == 0:
            out.append(inp[i])
        else:
            if inp[i] > out[-1]:
                out.append(inp[i])
            else:
                for j in range(len(out)):
                    if inp[i] <= out[j]:
                        out[j] = inp[i]
                        out[j+1:] = []
                        break
        max_len.append(len(out))
        print(f'{i+1} : {out}')
    return len(out)
k = LIS(inp)
print(f'longest increasing subsequence : {max(max_len)}')