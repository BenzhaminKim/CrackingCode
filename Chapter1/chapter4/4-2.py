class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def bst(arr):
    mid = len(arr)//2
    print(arr[mid])

if __name__ == "__main__":
    bst([1,2,3,4,5,6,7,8,9,10])