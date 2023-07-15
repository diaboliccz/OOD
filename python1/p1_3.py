# *** Fun with permute ***
# input : 1,2,3
# Original Cofllection:  [1, 2, 3]
# Collection of distinct numbers:
#  [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
print("*** Fun with permute ***")
value = input("input : ").split(",")
value = [int(i) for i in value]
print("Original Cofllection: ", value)

def permute(nums):
    result_perms = [[]]
    for n in nums:
        new_perms = []
        for perm in result_perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                result_perms = new_perms
    return result_perms

print("Collection of distinct numbers:\n",permute(value))