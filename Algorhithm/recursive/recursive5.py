def generate_permutations(s, k):
    if k == 0:
        yield ""
    else:
        for i in range(len(s)):
            for p in generate_permutations(s[:i] + s[i + 1:], k - 1):
                yield s[i] + p


def permute_string(s, k):
    if k < 0:
        return "Invalid value of k. k must be a non-negative integer."
    if k > len(s):
        return "Invalid value of k. k must be less than or equal to the length of s."
    else:
        return sorted(set(generate_permutations(s, k)))


inp = input("Enter a string and k: ").split("/")
s, k = inp[0], int(inp[1])
print((permute_string(s, k)))
