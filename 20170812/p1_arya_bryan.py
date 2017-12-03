import sys

def count_days(n, k, candies):
    days = 0
    valid_candies = 0

    if (k == 0): return 0
    for i in range(n):
        if candies[i] < 8:
            valid_candies += candies[i]
        else:
            valid_candies += 8
            if (i+1 < n): candies[i+1] += candies[i] - 8
        days += 1
        #print(days, candies[i], valid_candies)
        if valid_candies >= k:
            return days
    return -1

def main():
    (n,k) = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))
    candies = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))
    print(count_days(n, k, candies))

if __name__ == '__main__':
    main()
