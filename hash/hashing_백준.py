import sys

l = int(sys.stdin.readline())
hash_str = str(sys.stdin.readline())
sum = 0
for i in range(l):

    char = hash_str[i]
    sum = sum + (ord(char)-96)*(31**i)
    
hash = sum % 1234567891
print(hash)
