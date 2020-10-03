class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

def kth_linkedList(linkedList,k):
    if linkedList == None:
        return 0
    
    index = kth_linkedList(linkedList.next, k) + 1

    if index == k:
        print(linkedList.val, index)
    return index

if __name__ == "__main__":
    
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    kth_linkedList(n1,4)