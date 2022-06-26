from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())

hashmap = {}
for i in N:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1


print(" ".join(str(hashmap[m]) if m in hashmap else '0' for m in M))
