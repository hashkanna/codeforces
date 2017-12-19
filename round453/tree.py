from collections import defaultdict
n=int(input())
p=list(map(int, input().split()))
c=list(map(int, input().split()))

d=defaultdict(set)
for i,elem in enumerate(p):
    d[elem].add(i+2)
# print(d)

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# print(dfs(d, 6)) # {'E', 'D', 'F', 'A', 'C', 'B'}

dd=defaultdict(list)
for i in range(1,n+1):
    dd[i] = list(dfs(d,i))
# print(dd)

out_colors=[-1 for i in range(n)]
val=0
for k in sorted(dd, key=lambda k: len(dd[k]), reverse=True):
    # print(k, dd[k])
    if out_colors[k-1] != c[k-1]:
        val+=1
        for x in dd[k]:
            out_colors[x-1]=c[k-1]
print(val)
# print(out_colors)
