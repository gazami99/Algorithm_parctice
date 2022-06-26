def solution(n, arr1, arr2):
    answer = []
    
    space_list = [' ']*n      # 공백 리스트 생성 
    
    pwd = []
    
    for i in range(n):
        
        num_bin = bin(arr1[i] | arr2[i])    #두 값에대한 비트연산  or 연산 
        num_bin = num_bin[2:]             # 복호화에 필요없는 0b 제거
        
        if len(num_bin) < n:             # 비트연산에 사라진 자릿수 넣기
            
            num_bin = ' '*(n-len(num_bin))+num_bin
          
        num_bin = num_bin.replace('1','#')      #  복호화 작업 1 > # 0> 공백 
        num_bin = num_bin.replace('0',' ')
        
        pwd.append(num_bin)                      
    
    answer = pwd
    return answer
