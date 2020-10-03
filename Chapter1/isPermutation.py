from itertools import permutations

def isPermutation1(str1,str2):
    if len(str1) != len(str2):
        print(False)
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)

    if str1 == str2:
        print(True)
        return True
    else:
        print(False)
        return False

def isPermutation(str1, str2):
    if len(str1) != len(str2):
        print(False)
        return False
    char_set = [0 for _ in range(128)]

    for c in str1:
        char_set[ord(c)] += 1
    for c in str2:
        char_set[ord(c)] -= 1
        if char_set[ord(c)] < 0 :
            print(False)
            return False
    print(True)
    return True

if __name__ == "__main__":
    isPermutation('cbaa','ccab')