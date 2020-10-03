class Graph():
    def __init__(self):
        self.nodes = []

class Node():
    def __init__(self,value):
        self.value = value
        self.visited = False
        self.childeren = []

    def add_childeren(self,node):
        self.childeren.append(node)
        return self.childeren

    def __str__(self):
        return f"{self.value}"

def hasRoute(graph, start, end):
    queue = []
    
    queue.append(start)

    while len(queue) != 0:
        current = queue.pop(0)
        current.visited = True
        print(current)
        if current == end:
            print(True)
            return True
        for n in current.childeren:
            if n.visited == False:
                queue.append(n)
    print(False)
    return False
def dfs(node):
    if node == None:
        return 0
    node.visited = True
    print(node.value)
    for n in node.childeren:
        if n.visited == False:
            dfs(n)
    
if __name__ == "__main__":
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node0.add_childeren(node1)
    node0.add_childeren(node3)
    node3.add_childeren(node2)
    node3.add_childeren(node1)

    graph = Graph()
    graph.nodes.append(node0)
    graph.nodes.append(node1)
    graph.nodes.append(node2)
    graph.nodes.append(node3)

    hasRoute(graph,node0,node4)
