import sys

def num_digits(num_list, count_digits):

    num1 = sorted(num_list[:3])
    num2 = sorted(num_list[3:])
    diff = sum(num1) - sum(num2)
    print(num_digits, num1, num2)
    if diff == 0:
        return count_digits
    else:
        count_digits += 1
        if diff > 0:
            if num2[0] + diff > 9:
                num2[0] = 9
            else:
                num2[0] = num2[0] + diff
            num_digits(num1 + num2, count_digits)
        else:
            if num1[0] + abs(diff) > 9:
                num1[0] = 9
            else:
                num1[0] = num1[0] + diff
            num_digits(num1 + num2, count_digits)

def main():
    num = sys.stdin.readline().strip()
    num_list = [int(d) for d in num]
    print(num_digits(num_list, count_digits=0))

if __name__ == '__main__':
    main()
