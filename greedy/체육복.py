def solution(n, lost, reserve):
    
    answer = 0
    
    reserve.sort()
    lost.sort()

    for i in reserve:
        
        i_left  = (i-1)
        i_right = i+1
        
        if i in lost:
            lost.remove(i)
            
        elif i_left in lost:
        
            lost.remove(i_left)
            
        elif not i_right in reserve and  i_right in lost:
            
            lost.remove(i_right)
     
    answer = n-len(lost)
    
    return answer
