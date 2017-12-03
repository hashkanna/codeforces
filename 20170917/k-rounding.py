import sys

def krounding(n,k):
    c = 1
    while True:
        val = (c*(pow(10,k))) % n
        if val == 0:
            return c*(pow(10,k))
        c+=1

def main():
    (n,k) = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))
    print(krounding(n,k))

if __name__ == '__main__':
    main()
