import sys
import heapq as h



def dijkstra(start):
    
    q = []
    cost[start] = 0
    
    h.heappush(q,[0,start])
    
    while q:
        
        pos_cost,pos = h.heappop(q)
        for i in graph[pos]:
            
            tmp_cost = pos_cost + 1
            
            if tmp_cost < cost[i]:
                
                cost[i] = tmp_cost
                h.heappush(q,[tmp_cost,i])
                
    return [i+1 for i in range(N) if cost[i]==K]                
           
            
            
        
    




N, M, K, X = map(int,sys.stdin.readline().split())

max_size = sys.maxsize

graph = [[] for _ in range(N)]
cost  = [max_size for _ in range(N)]

for _ in range(M):
    
    a,b = map(int,sys.stdin.readline().split())
    
    graph[a-1].append(b-1)
    
  
    
node_list = dijkstra(X-1)
node_list.sort()

if node_list:
    
    print("\n".join(str(i) for i in node_list))
    
    
else:
    
    print('-1')
