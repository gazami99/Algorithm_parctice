from sys import stdin
_ = stdin.readline()
n = list(map(int,stdin.readline().split()))
_ = stdin.readline()
m = list(map(int,stdin.readline().split()))


dict_m = {i:0 for i in m}


for i in n:
    
    if i in dict_m:
        
        dict_m[i] = dict_m[i] + 1
        
print(' '.join(str(dict_m[i]) for i in m))
