import sys

n = int(sys.stdin.readline())


def base_2(number,decimal):
    
    if number < 2:
        
        return 1*10**decimal
    
    return (number % 2)* (10**decimal) + base_2(int(number/2),decimal+1)


print(base_2(n,0))
