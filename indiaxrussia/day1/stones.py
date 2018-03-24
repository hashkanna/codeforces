
# dp[0]=[0]
# dp[1]=1
# dp[2]=1
# dp[3]=2
dp=[0,1,1,2]
for i in range(4,101):
    choices=[]
    if i%3==0:
        choices=[1,2]
    elif (i-1)%3==0:
        choices=[1,3]
    elif (i-2)%3==0:
        choices=[1,2,3]
    # print([dp[i-j] for j in choices])
    dp.append(1 if 2 in [dp[i-j] for j in choices] else 2)
n=int(input())
print(dp[n])
# print(dp)
