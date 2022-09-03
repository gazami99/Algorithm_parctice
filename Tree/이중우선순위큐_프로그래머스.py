import heapq

def solution(operations):
    
    answer = [0,0]
    max_num = 0
    q = []
    
    for i in operations:
        
        if i[0] == "I":
            
            heapq.heappush(q,int(i[1:]))
            
        elif q and i[0] == "D":
            
            if i[2] == "-":
                
                heapq.heappop(q)
            
            else:
                
                max_num = max(q)
                q.remove(max_num)
    
    if q:
        answer[0] = max(q)
        answer[1] = q[0]
    
    return answer
