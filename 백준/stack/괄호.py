import sys

N = int(sys.stdin.readline())

par_list  =[]
test  =[]

for _ in range(N):

    tmp = map(str,sys.stdin.readline().rstrip())
    par_list.append(list(tmp))
    

for i in par_list:
    
    tmp_test = 0
    
    for j in i:
        
        if j == "(":
            
            tmp_test += 1
            
        else:
            
            tmp_test += -1
        
        if tmp_test <0:
            break
        
    if tmp_test == 0:
        test.append("YES")
    else:
        test.append("NO")
    
    
print("\n".join(str(i) for i in test))
