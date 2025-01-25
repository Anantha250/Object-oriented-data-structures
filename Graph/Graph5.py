class Graph:
    def __init__(self):
        self.edge = [[] for _ in range(1000)]
        self.root = [i for i in range(1000)]
        self.color = [0 for _ in range(1000)]

    def parent(self, u):
        if self.root[u] != u:
            self.root[u] = self.parent(self.root[u])
        return self.root[u] 
    
    def union(self, u, v):
        self.root[self.parent(u)] = self.parent(v)

    def add(self, u, v):
        self.edge[u].append(v)

    def dfs(self, u):
        if self.color[u] == 1:
            return True
        if self.color[u] == 2:
            return False
        
        self.color[u] = 1
        for v in self.edge[u]:
            if self.dfs(v):
                return True
        self.color[u] = 2
    
    def check(self):
        for u in range(1000):
            if self.dfs(u):
                return True
        return False




inp = [[int(k) for k in e.split()] for e in input("Enter : ").split(',')]
g = Graph()
flag = False
for u, v in inp:
    g.add(u, v)

if g.check():
    print("Graph has a cycle")
else: 
    print("Graph has no cycle")
