import collections as col

from sys import stdin

def dfs(n,path_l):   # 시작점과 , 빈 리스트 추가
    
      
    path_l.append(n)     #  경로 추가 
    for i in graph[n]:      # 다음 추가 경로 지정
        if not i in path_l: #  지나간 경로가 아닐시 자기자신을 재호출 
            path_l = dfs(i,path_l) # 호출한 함수를 저장 
    
    return path_l        # 경로값 반환 

def bfs(n,path_l):      # 시작점 ,빈 리스트 추가
    
    queue = col.deque([n])        # 큐에 시작점 추가
    path_l.append(n)               #  경로값 저장
    while queue:                    # 큐가 없어질때까지 반복
        q = queue.popleft()         # 큐 값 추출
        for i in graph[q]:          #  현재 경로에대한 다음경로 모두 저장
            if not i in path_l:     #  이미 지나간 그래프가 아닐시 경로값에 모두 저장하고 다음 경로값을 큐에 저장
                queue.append(i)
                path_l.append(i)
     
    return path_l                   # 경로값 반환 


"""
재귀형 bfs

    path_l.append(n)    
    for i in graph[n]:     
        if not i in path_l: 
            path_l.append(i)  
    
    k =  path_l.index(n)
    
    if not k < len(path_l):
        
        path_l = bfs(path_l[k+1],path_l)
     
    return path_l
"""



###
N, M, V = map(int, stdin.readline().split())


graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1,N+1):
    graph[i].sort()
    

    
dfs_path = dfs(V,[])
bfs_path = bfs(V,[])

print(" ".join(str(i) for i in dfs_path))
print(" ".join(str(i) for i in bfs_path))
