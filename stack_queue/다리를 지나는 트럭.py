def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    queue = []
    
    sum_w = 0
    
    br_len  = bridge_length
    
    time = br_len
    
    answer = time
    
   
    for t_w in (truck_weights):
        
        time = time + 1
        sum_w = sum_w + t_w
        
   
        while queue and (sum_w> weight or (time-br_len) >= queue[0][0]):
            
            tmp = queue.pop(0) # list 시간복잡도 O(n) 하지만 queue라 생각하기 
            sum_w = sum_w - tmp[1]
            
          
            time = tmp[0] + br_len
     
   
        
        queue.append([time,t_w])
        
        print(queue)
      
 
    answer = time
    return answer
