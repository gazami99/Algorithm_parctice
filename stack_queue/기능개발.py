import math

def solution(progresses, speeds):
    answer = []
    stack  = []
    
    for i in range(len(progresses)):
        
        work =  progresses[i]
        spd  =  speeds[i]
        
        r_day =  math.ceil((100-work) / spd)
        
        if not stack or tmp < r_day:
            
            tmp = r_day
            stack.append([1,r_day])
            
        else:
            
            stack[-1][0] = stack[-1][0]+1
            
            
        
        
    
    answer =  [stack[i][0] for i in range(len(stack))]
    
    print(stack)

    return answer
