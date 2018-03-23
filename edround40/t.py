# heeye
n = int(input())
s = input()
# print(range(n/2,0,-1))
i=0
for l in range(n//2,0,-1):
    for j in range(i+l,n-l+1):
        if s[i:i+l] == s[j:j+l] :
            print(n-l+1)
            exit(0)
print(n)
