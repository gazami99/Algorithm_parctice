import sys

N = int(sys.stdin.readline())

stairs = []

for i in range(N):
    
    tmp = int(sys.stdin.readline())
    
    stairs.append(tmp)
    


if N>2:

    S0 = stairs[0]
    S1 = stairs[1]+stairs[0]
    S2 = max(stairs[2]+stairs[1],stairs[2]+stairs[0])

    S_list = [S0,S1,S2]

    for i in range(3,N):

        tmp = stairs[i]

        S = max(S_list[i-3]+stairs[i-1]+tmp,S_list[i-2]+tmp)

        S_list.append(S)



    print(S_list[-1])
    
else:
    
    print(sum(stairs))
    

