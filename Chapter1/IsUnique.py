#1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
#cannot use additional data structures?
#Hints: #44, # 777, # 7 32 

def isUnique(characters):
    hashTable = {}
    for character in characters:
        hashTable[character] = 0
    for c in characters:
        hashTable[c] += 1
    for key in hashTable:
        if hashTable[key] > 1:
            return False
    return True


def isUniqueCharacter(chars):
    checker = 0
    vals = []
    for c in chars:
        val  = ord(c) - ord('a')
        if (checker & ( 1 << val) >=1):
            return False
        print(checker,checker & ( 1 << val),1 << val)

        checker |= (1<<val)
        #print(int(val))
    return True
def isUniqueCharacter1(chars):
    char_set = [False for _ in range(128)]
    if len(chars)>128:
        return False
    for c in chars:

        if char_set[ord(c)] == False:
            return False
        else:
            char_set[ord(c)] = True
    return True
if __name__ == "__main__":
    #print(isUnique('abc'))
    print(isUniqueCharacter('abcc'))