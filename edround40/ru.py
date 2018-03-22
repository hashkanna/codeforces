n=int(input())
s=list(input())

count=0
i=0
while i<n-1:
    if s[i]!=s[i+1]:
        count+=1
        i+=2
    else:
        count+=1
        i+=1

while i<n:
    count+=1
    i+=1

print(count)
