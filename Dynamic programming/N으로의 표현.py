def solution(N, number):
    answer = 0
    dp  = [[] for i in range(8)]
    
    dp[0] = [N]
    dp[1] = [N+N,N*N,int(N/N),int(str(N)+str(N))] #exception  N-N = 0 
    
    for i in range(2):
        
        if number in dp[i]:
        
            return i+1
        
    
    for i in range(2,8):
        
        tmp_list =[int(str(N)*(i+1))]
        
        for j in range(int((i)/2)):
            

            tmp_list_dp1 = dp[i-j-1]
            tmp_list_dp2 = dp[j]
            
            for k in tmp_list_dp1:
                
                for m in tmp_list_dp2:
                    
                    tmp_list.append(k+m)
                    tmp_list.append(k*m)
                    
                    tmp_mul = k-m
                    
                    tmp_div = k/m
                    
                    if tmp_mul:
                        
                        tmp_list.append(abs(tmp_mul))
                    
                    if int(tmp_div):
                        
                        tmp_list.append(int(tmp_div))


        if number in tmp_list:
            
            return i+1
        else:
            
            dp[i] = list(set(tmp_list))
        
    return -1
