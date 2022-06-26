from sys import stdin



num_list = '0123456789'   #문자열 숫자 


n, base = map(str,stdin.readline().split())

decimal_n = 0
i = 0
base = int(base)
n = list(n)    ## 문자값을 정수화 ,리스트화
while n:    # n 리스트 추출 
    
    tmp = n.pop()
    
    if tmp in num_list:     # 문자가 숫자라면 숫자정수화
        tmp = int(tmp)
    else:                   # 숫자가아니라면 대문자 알파벳이므로 ascii 코드를 이용(숫자가 연속적이기 때문)
        tmp = ord(tmp) - 55
        
    decimal_n = decimal_n+ tmp * (base ** i)   ## 십진법 전환 n*(진법^자릿수)
    i += 1
    
print(decimal_n)
    
    
