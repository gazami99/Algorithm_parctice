import collections as col
from sys import stdin

def bfs(n):
    
    queue = col.deque([n])
    pass_list[n] = True
    num = 0
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if not pass_list[i]:
                queue.append(i)
                pass_list[i] = True
                num += 1
                
     
    return num


###
N = int(stdin.readline())
M = int(stdin.readline())
V=1

graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1,N+1):
    graph[i].sort()
    

    
pass_list = [False]*(N+1)

print(bfs(V))
