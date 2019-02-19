import numpy as np

class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []

    def add_edge(self, pair):
        start,end = pair
        if start in self.nodes:
            if end in self.nodes:
                self.edges[start].append(end)
                return 1
        else:
            return -1

    def children(self,node):
        return self.edges[node]

    def nodes(self):
        return str(self.nodes)

    def __str__(self):
        return str(self.edges)

    def add_node(self, n):
        if n in self.nodes:
            return -1
        else: 
            self.nodes.append(n)
            self.edges[n] = []
            return 1

    def del_node(self, n):
        if n in self.nodes:
            del self.nodes[n]
            del self.edges[n]
            return 1
        else: 
            return -1

    def del_edge(self, pair):
        x,y = pair
        if y in self.edges[x]:
            print(self.edges[x])
            self.edges[x].remove(y)
        return 1

    def reachable(self, nodes, pair1, pair2):
        x,y = pair1
        a,b = pair2
        if x in self.nodes:
            if y in self.nodes:
                if a in self.nodes:
                    if b in self.nodes:
                        return 1
        else: 
            return -1


a = np.zeros ((4,4),dtype = int)
a[0][1] = 1
a[1][2] = 1
a[2][3] = 1
print(a)
a = np.dot (a,a) + a
print(a)
a = np.dot (a,a) + a
print(a)

for i in range(0,4):
    for j in range(0,4):
        if not i == j:
            print("{0} reaches {1}: {2}".format(i+1,j+1,bool(a[i][j])))

g = Graph([0,1,2,3])
print(g) #test
g.add_edge((1,3))
print(g) #test
g.add_node(4)
print(g) #test
g.add_edge((4,2))
print(g) #test
g.del_node(0)
print(g) #test
g.del_edge((1,3)) 
print(g) #test 