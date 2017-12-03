import sys
from operator import itemgetter

def is_possible(shows_list):
    sorted_shows_list = sorted(shows_list, key=itemgetter(1))
    #print(sorted_shows_list)
    A = 0
    B = 0
    for i in sorted_shows_list:
        #print(A, B)
        if i[0] >= A:
            A = i[1] + 1
        elif i[0] >= B:
            B = i[1] + 1
        else:
            return "NO"
    return "YES"

def main():
    n = int(sys.stdin.readline().strip())
    shows_list = []
    for i in range(n):
        (l,r) = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))
        shows_list.append((l,r))
    print(is_possible(shows_list))

if __name__ == '__main__':
    main()
