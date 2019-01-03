def area(x1, y1,  x2,  y2, x3,  y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0);

def check(x1,  y1,  x2,  y2,  x3, y3,  x4,  y4,  x,  y):
    A = area(x1, y1, x2, y2, x3, y3) + area(x1, y1, x4, y4, x3, y3)
    A1 = area(x, y, x1, y1, x2, y2)
    A2 = area(x, y, x2, y2, x3, y3)
    A3 = area(x, y, x3, y3, x4, y4)
    A4 = area(x, y, x1, y1, x4, y4);
    return (A == A1 + A2 + A3 + A4);


n,d = list(map(int, input().split()))
nn = int(input())
for i in range(nn):
    x,y=list(map(int, input().split()))
    if (check(0, d, d, 0, n, n-d, n-d, n, x, y)):
        print("YES")
    else:
        print("NO")
