a=input()
links=a.count('-')
pearls=a.count('o')
if links==0 or pearls==0:
    print("YES")
elif links%pearls==0:
    print("YES")
else:
    print('NO')
