class Queue:
    def __init__(self):
        self.lst = []
    
    def pop(self):
        if not self.isEmpty():
            return self.lst.pop(0)
        else:
            return None
    
    def enqueue(self, item):
        self.lst.append(item)
    
    def __str__(self):
        return str(self.lst)
     
    def isEmpty(self):
        return len(self.lst) == 0

    def dequeue(self):
        return self.lst.pop()

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []
    
    def add_edge(self, pair):
        start, end = pair
        self.edges[start].append(end)
            
    def children(self, node):
        return self.edges[node]

    def __str__(self):
        finalString = ""
        for n in self.nodes:
            finalString += str(n) + " -> " + str(self.edges[n]) + "\n"
        return finalString
 
    def __getitem__(self,key):
        return 0




def bfsfull(g,node):
    visited = []
    unvisted = [g.children]
    q = Queue()
    q.enqueue(node)

    while not q.isEmpty():
        newNode = q.dequeue()
        if newNode not in visited:
            print(newNode)            
            visited.append(newNode)
            list = g.children(newNode)
            for n in list:
                if n not in visited:
                    q.enqueue(n)

        if q.isEmpty() and len(visited) != len(g.nodes):
            for i in g.nodes:
                if i not in visited:
                    q.enqueue(i)
                    break


g = Graph([1,2,3,4,5,6,7,8])
elst = [(1,2),(1,3),(2,8),(3,5),(3,4),(5,6),(6,4),(6,7)]
for i in elst:
    g.add_edge(i)
print(g.edges)
bfsfull(g,5)