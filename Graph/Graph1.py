inp = input("Enter : ").split(',')

inp = [e.split() for e in inp]
s = set()
for i in inp:
    s.add(i[0])
    s.add(i[1])

lst = sorted(s)
n = len(lst)

arr = [[0 for e in range(n)] for e in range(n)]
for u,v in inp:
    uid = lst.index(u)
    vid = lst.index(v)
    arr[uid][vid] = 1

print(f"    ", end="")
[print(e, end="  ") for e in lst]
print()
for i, val in enumerate(lst):
    print(f"{val} : ", ", ".join([str(e) for e in arr[i]]), sep="")
