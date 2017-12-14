def chunks(m):
    f=0
    if m%3==0 or m%7==0:
        return("YES")
    else:
        for j in range(1,34):
            for k in range(1,16):
                if 3*j + 7*k == m:
                    return("YES")

    return("NO")

n=int(input())
for i in range(n):
    m=int(input())
    print(chunks(m))
