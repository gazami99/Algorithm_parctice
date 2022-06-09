import math

def solution(answers):
    answer = []
    
    rank_list= [0,0,0] # 수포자 1번 2번 3번 정답 
    
    ans_len = len(answers)
    
    max_num = 0
    
    num1_list = [1,2,3,4,5]*math.ceil(ans_len/5) # 반복자 크기 만큼 
    num2_list = [2,1,2,3,2,4,2,5] * math.ceil(ans_len/8)
    num3_list = [3,3,1,1,2,2,4,4,5,5] * math.ceil(ans_len/10)
    
    del num1_list[ans_len:]  # 정답크기에 맞게 컷 
    del num2_list[ans_len:]
    del num3_list[ans_len:]
    
    
    

    
    for i in range(ans_len):
        
        tmp_ans = answers.pop()  
        tmp1 = num1_list.pop()
        tmp2 = num2_list.pop()
        tmp3 = num3_list.pop()
        
        rank_list[0] = rank_list[0] + int(tmp_ans == tmp1)
        rank_list[1] = rank_list[1] + int(tmp_ans == tmp2)
        rank_list[2] = rank_list[2] + int(tmp_ans == tmp3)
        
        
        
        
     
    max_num = max(j for j in (rank_list))
    answer = [i+1 for i, j in enumerate(rank_list) if j == max_num]
    
    return answer
