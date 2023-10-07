
inp = input('Enter str1,str2: ').split(',')
str1 = inp[0]
str2 = inp[1]
def isIsomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        for i in range(len(str1)):
            if str1.count(str1[i]) != str2.count(str2[i]):
                return False
        return True
if isIsomorphic(str1,str2):
    print(f'{str1} and {str2} are Isomorphic')
else:
    print(f'{str1} and {str2} are not Isomorphic')