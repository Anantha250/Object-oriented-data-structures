class Graph:
    def __init__(self):
        self.node = set()
        self.edge = {}
    
    def add(self, u, w, v):
        self.node.add(u)
        self.node.add(v)
        if u not in self.edge:
            self.edge[u] = []
        self.edge[u].append([w, v])

    def dijkstra(self, start, target):
        if start not in self.node or target not in self.node:
            print("Not have path :", f"{start} to {target}")
            return
        for key in self.edge.keys():
            self.edge[key].sort(key=lambda x: x[0])
        dist = {_:float('inf') for _ in self.node}
        prev = {_:None for _ in self.node}
        visit = {_:False for _ in self.node}
        q = [start]
        dist[start] = 0
        while q:
            u = q.pop(0)
            if visit[u] or u not in self.edge:
                continue
            visit[u] = True
            for w, v in self.edge[u]:
                q.append(v)
                if w+dist[u] < dist[v]:
                    dist[v] = w+dist[u]
                    prev[v] = u
        
        if dist[target] == float('inf'):
            print("Not have path :", f"{start} to {target}")
            return
        print(f"{start} to {target} : ", end="")
        cur = target
        ans = [target]
        while prev[cur]:
            ans.insert(0, prev[cur])
            cur = prev[cur]
        print("->".join(ans))


g = Graph()
inp, path = input("Enter : ").split('/')
inp = [e.split() for e in inp.split(',')]
path = [e.split() for e in path.split(',')]
for u,w,v in inp:
    g.add(u, int(w), v)
for u,v in path:
    g.dijkstra(u,v)



