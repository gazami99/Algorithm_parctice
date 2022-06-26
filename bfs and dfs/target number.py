import collections as col

def solution(numbers, target):
    answer = 0
    
    num_sum = sum(numbers)
    
    num_case = 0

    num_deque = col.deque()  ### deque  BFS
    
    minus_target =  int((num_sum - target)/2) #  모두 더한다음 선택해서  빼주기 
    
    comb_size = 0
    
    for k in range(len(numbers)):
        
        i = numbers.pop()
        
        if i >= minus_target:    # target 과 같거나 크면 가능한 조합수에서 제외 
            
            num_case += int(i==minus_target) # 같다면 경우 1로서 case 증가 다음 숫자값에대해 넘김
            continue
     
        loop = num_deque.copy() # num_deque 는 for문에서  변형되기때문에 그전 값들을  복사 
        
        for j in loop:
            
         
            tmp = num_deque.popleft()        # queue 역할 
            tmp_sum = tmp +i                 # queue 값과 현재 숫자값을 더해서 조합 
            num_deque.append(tmp)            # queue  다음 조합에 쓰이므로 다시 큐값에 넣어줌 
            
            
            if tmp_sum < minus_target:       
                
                num_deque.append(tmp_sum)    # target 값ㅇ보다 작으면 다음 조합에 case 증가하므로 큐값에 넣어준다
              
                
            elif tmp_sum == minus_target:    # target 발견 
                
                num_case += 1
                
        num_deque.append(i)                  # 다음 target 조합을위해 숫자값을 큐값에 넣어줌 
     
                
    answer = num_case
    return answer
