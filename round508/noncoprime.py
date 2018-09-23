n=int(input())

ans=0
val=sum(range(1,n+1))
if n>1:
    for i in range(2,n+1):
        if (val-i)%i==0:
            ans=i
            break
if ans==0:
    print("No")
else:
    print("Yes")
    print("1 " + str(ans))
    ans_set=[str(x) for x in range(1,n+1) if x!=ans]
    print(str(n-1) + " " + " ".join(ans_set))
