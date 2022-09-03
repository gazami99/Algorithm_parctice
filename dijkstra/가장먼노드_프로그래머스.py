import sys
import heapq
    
def dijkstra(start):
    q = []
    cost[start] = 0
    heapq.heappush(q,[0,start])
    
    
    while q:
        
      
        
        size,pos = heapq.heappop(q)
        
        for i in graph[pos]:
            
            tmp_cost = size+1
            
            if cost[i] > tmp_cost:
                
                cost[i] = tmp_cost            
                heapq.heappush(q,[tmp_cost,i])
                
    return max(cost)
                
            
 
    
    
                
def solution(n, edge):
    
    global graph,cost,max_size

    answer = 0
    max_size = sys.maxsize
    
    
    graph = [[] for i_ in range(n)]
    cost = [max_size for _ in range(n)]
 

    for i in edge:
        
        graph[i[0]-1].append(i[1]-1)
        graph[i[1]-1].append(i[0]-1)
        
    
    m = dijkstra(0)
    
    answer = cost.count(m)
   
    return answer


