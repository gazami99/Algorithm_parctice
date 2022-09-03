from collections import deque

def solution(priorities, location):
    
    answer = 0
    size = len(priorities)
    
    deq = deque([[priorities[i],i] for i in range(size)])
    regStack = []

    while deq:
        
        max_tmp = max(deq)[0]
        tmp = []
        
        for _ in range(len(deq)):
            
            tmp = deq.popleft()
            deq.append(tmp)
            if tmp[0]== max_tmp :               
                break
            
            
        regStack.append(deq.pop())
    
    
    answer = regStack.index([priorities[location],location])+1
    return answer
