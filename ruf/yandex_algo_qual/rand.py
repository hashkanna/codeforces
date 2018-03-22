a = set(map(int,input().split()))
n = int(input())
for i in range(n):
    l=list(map(int,input().split()))
    c=0
    r="Unlucky"
    for j in l:
        if j in a:
            c+=1
            if c==3:
                r="Lucky"
                break
    print(r)
