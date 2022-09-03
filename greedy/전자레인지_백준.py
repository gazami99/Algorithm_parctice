import sys


[T] = map(int,sys.stdin.readline().split())

Buttons = [300,60,10]
Buttons_count = [0 for _ in range(3)]

for i in range(3):
    
    tmp_Button = Buttons[i]
    tmp_count     = T/tmp_Button
    tmp_remainder = T%tmp_Button
    
    Buttons_count[i] = int(tmp_count)
    
    T = int(tmp_remainder)
    
if not T:
    
    print(" ".join(str(i) for i in Buttons_count))
    
else:
    
    print(-1)
