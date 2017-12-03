s=input()
A=[i for i, letter in enumerate(s) if letter == 'A']
Q=[i for i, letter in enumerate(s) if letter == 'Q']

val=0
for i in A:
    val+=(sum(x<i for x in Q) * sum(x>i for x in Q))
print(val)
