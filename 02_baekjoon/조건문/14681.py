x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)    
    
'''중첩 조건문
if x > 0:
    if y > 0: print(1)
    else: print(4)
else:
    if y > 0: print(2)
    else: print(3)
'''