import sys

def max_split(a):
    if a in [1,2,3,5,7,11]:
        return -1
    if a%4==0:
        return a//4
    if a%4==2:
        return 1 + ((a-6)//4)
    if a%4==1:
        return 1 + ((a-9)//4)
    if a%4==3:
        return 2 + ((a-15)//4)

def main():
    n = int(sys.stdin.readline().rstrip('\n'))
    b = []
    for i in range(n):
        b.append(int(sys.stdin.readline().rstrip('\n')))
    for a in b:
        print(max_split(a))

if __name__ == '__main__':
    main()
