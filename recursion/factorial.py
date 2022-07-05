import sys

n = int(sys.stdin.readline())


def factorial(number):
    
    if number==0:
        
        return 1
    
    return number*factorial(number-1)


print(factorial(n))
        
