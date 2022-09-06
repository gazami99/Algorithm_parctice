def solution(board, moves):
    answer = 0
    stack = []
    count = 0
    
    for i in moves:
        
        for j in board:
            
            if j[i-1] != 0:
                
                tmp = j[i-1]
                j[i-1] = 0
                
                if stack and tmp == stack[-1]:
                    
                    stack.pop()
                    count += 2
                else:
                    stack.append(tmp)
                
                break
                
            
    answer = count
    return answer
