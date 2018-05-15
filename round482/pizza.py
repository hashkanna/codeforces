n=int(input())
n+=1
# `print(bin(n)[:2])
# `print(bin(n).count('1'))
if bin(n)[2]=='1' and bin(n).count('1')==1:
    print(len(bin(n))-3)
else:
    print(n)
