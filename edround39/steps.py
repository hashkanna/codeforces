# If a = 0 or b = 0, end the process. Otherwise, go to step 2;
# If a ≥ 2·b, then set the value of a to a - 2·b, and repeat step 1. Otherwise, go to step 3;
# If b ≥ 2·a, then set the value of b to b - 2·a, and repeat step 1. Otherwise, end the process.

a,b=list(map(int,input().split()))
flag=0
while(flag==0 and a!=0 and b!=0):
    if(a>=2*b):
        diff=a-(2*b)
        a-=(diff-(diff%(2*b)))
        if(a>=2*b):
            a-=(2*b)
    elif(b>=2*a):
        # b-=(2*a)
        diff=b-(2*a)
        b-=(diff-(diff%(2*a)))
        if(b>=2*a):
            b-=(2*a)
    else:
        flag=1

print(a,b)
    
