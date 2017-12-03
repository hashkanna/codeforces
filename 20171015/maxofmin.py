import sys

def maxofmin(a,n,m):
    if m==1:
        return min(a)
    elif m==2:
        return max(a[0], a[-1])
    else:
        return max(a)

def main():
    n,m = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))
    a = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))
    print(maxofmin(a,n,m))

if __name__ == '__main__':
    main()
