def solution(N, road, K):
    answer = 0
    max_size = sum([i[2] for i in road])
    
    cost_list =[max_size for _ in range(N)]
    cost_list[0] = 0
    
    visited = [False for _ in range(N)]
    visited[0] = True
    start = 0
    
    while False in visited:
        
        min_cost = max_size
        
        for i in road:
            
            if (start+1) in i[:2]:
            
                tmp_idx = i[0]+i[1]-(start+1)-1
                
                tmp_cost = i[2] + cost_list[start]
                            
                cost_list[tmp_idx] = min(tmp_cost,cost_list[tmp_idx])
                
        
        for i in range(N):
            
            tmp_cost = cost_list[i]
            Check    = visited[i]
            
            if not Check and (tmp_cost <= min_cost):
                
                min_cost = tmp_cost
                start = i
            
        
        visited[start] = True
                
     
    for i in cost_list:
        
        if i <=K:
            
            answer +=1
        
    


    return answer
