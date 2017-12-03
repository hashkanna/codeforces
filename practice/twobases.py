n, bx = list(map(int, input().split()))
x = list(map(int, input().split()))
m,by = list(map(int, input().split()))
y = list(map(int, input().split()))

X=sum(x[i] * bx**(n-i-1) for i in range(n))
Y=sum(y[i] * by**(m-i-1) for i in range(m))
# print(X, Y)
print('<' if X<Y else ('>' if X>Y else '='))
