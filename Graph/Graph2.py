inp = [e.split() for e in input("Enter : ").split(',')]
lst = []
for i in inp:
    u = ord(i[0]) - ord("A")
    v = ord(i[1]) - ord("A")
    while len(lst) < u+1 or len(lst) < v+1:
        lst.append([])
    
    lst[u].append(v)
    lst[v].append(u)

for i in range(len(lst)):
    lst[i].sort()

ans = []
def dfs(u):
    if u in ans:
        return
    ans.append(u)
    for v in lst[u]:
        if v not in ans:
            dfs(v)

ans_b = []
def bfs(start):
    q = [start]
    while q:
        u = q.pop(0)
        if u in ans_b:
            continue
        ans_b.append(u)
        for v in lst[u]:
            q.append(v)

for i in range(len(lst)):
    dfs(i)
    bfs(i)
print("Depth First Traversals :", " ".join([chr(e +ord("A")) for e in ans]))
print("Bredth First Traversals :", " ".join([chr(e +ord("A")) for e in ans_b]))