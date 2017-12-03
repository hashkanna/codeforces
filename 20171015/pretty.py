import sys

def pretty(a,b):
    for i in range(1,10):
        if i in a and i in b:
            return i
    if min(a) < min(b):
        return min(a)*10+min(b)
    else:
        return min(b)*10+min(a)

def main():
    n,m = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))
    a = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))
    b = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))
    print(pretty(a,b))

if __name__ == '__main__':
    main()
