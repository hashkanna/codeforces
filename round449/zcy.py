k,p = list(map(int, input().split()))
count=0
val=0
# n = 10
# while True:
#     if len(str(n))%2==0 and str(n) == str(n)[::-1]:
#         val = (val + (n%p))%p
#         count+=1
#     if count==k:
#         print(val)
#         break
#     n+=1

for i in range(1, k+1):
    s = str(i) + str(i)[::-1]
    val = (val + ( int(s)% p)) % p
    # print(val)
print(val)
