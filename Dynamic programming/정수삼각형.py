def solution(triangle):
    
    floor = triangle.pop()
    
    if triangle:
        
        for i in range(len(triangle[-1])):
            
            max_num = max(floor[i],floor[i+1])
            triangle[-1][i] = triangle[-1][i]+max_num
            
        return solution(triangle)
    
    else: 
        
        return floor[-1]
    
    
    
