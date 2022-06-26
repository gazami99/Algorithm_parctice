from sys import stdin

num_list = [[]] # 조건문을위해 임의 [] 값 대입

while not num_list[-1] == [0]:
    
    tmp_list = list(map(int,stdin.readline().strip()))
    num_list.append(tmp_list)

num_list.remove([])  # 첫번째 값 제거
num_list.pop()      # 0값은 계산에서 제외이므로 제거

for i in num_list:
    fact =1         # 팩토리얼 계수 
    num_sum=j = 0   # 숫자 합 , 계수값 선언

    while i:        # 숫자 리스트 모두 잇을ㄹ때까지
        j  += 1
        tmp = i.pop()
        
        fact = fact*1*j   ## 팩토리얼 1*2*3 ....
        num_sum = num_sum +tmp*fact  # 팩토리얼 총합 
    print(num_sum) # 출력 
