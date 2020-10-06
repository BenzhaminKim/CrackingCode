class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def bst(arr):
    bst1(arr,0,len(arr)-1)

def bst1(arr,start,end):
    if start > end:
        return
    
    mid = (start + end) // 2
    node = Node(arr[mid])
    node.left = bst1(arr,start,mid-1)
    node.right = bst1(arr,mid+1,end)
    print(node.value)
    return node

if __name__ == "__main__":
    bst([1,2,3,4,5,6,7,8,9,10])